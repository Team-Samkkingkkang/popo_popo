import json

from django.db.models import Sum, Max
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from . import models
# Create your views here.


from main.models import Diary, User, UserImage, Qna, Product, ProductOption, Order, OrderCount
from main.forms import CommentForm


def diary(request):
    return render(request, 'diary_page/diary.html', context={})


@login_required(login_url="/account/")
def diary_create(request):
    if request.method == 'POST':

        diary_model = Diary()
        diary_model.user = request.user
        if request.FILES:
            diary_img = request.FILES['diary_img']
            diary_model.diary_img = diary_img

        if request.POST.get('diary_content'):
            diary_content = request.POST.get('diary_content')
            diary_model.diary_content = diary_content
            diary_model.save()

        else:
            context = {'message': '일기 내용이 없습니다.'}
            return render(request, 'diary_page/diary_create.html', context)

        return HttpResponseRedirect(reverse('main:diary_show'))
    return render(request, 'diary_page/diary_create.html', context={})


@login_required(login_url="/account/")
def diary_show(request):
    diarys = Diary.objects.filter(user=request.user)
    return render(request, 'diary_page/diary_show.html', context={'diarys': diarys})


def diary_detail(request):
    return render(request, 'diary_page/diary_detail.html')


def share_status(request):
    if request.GET['share_status'] == 'True':
        Diary.objects.filter(pk=request.GET['share_id']).update(diary_share_state=True,
                                                                diary_share_date=timezone.localtime())
        context = {'share': 'True'}

    elif request.GET['share_status'] == 'False':
        Diary.objects.filter(pk=request.GET['share_id']).update(diary_share_state=False,
                                                                diary_share_date=timezone.localtime())
        context = {'share': 'False'}
    else:
        print('no!')
        context = {'share': 'no'}
    return JsonResponse(context)


def diary_delete(request, diary_id):
    print(diary_id)
    Diary.objects.filter(id=diary_id).delete()
    return HttpResponseRedirect(reverse('main:diary_show'))


def diary_update(request, diary_id):
    context = {}
    diary = Diary.objects.get(id=diary_id)
    context['diary'] = diary

    if request.method == 'POST':
        if request.FILES:
            diary_img = request.FILES['diary_img']
            Diary.objects.filter(pk=diary_id).update(diary_img=diary_img)

        if request.POST.get('diary_content'):
            diary_content = request.POST.get('diary_content')
            Diary.objects.filter(pk=diary_id).update(diary_content=diary_content)
            return render(request, 'diary_page/diary_detail.html', context)
        else:
            context['message'] = '일기 내용이 없습니다.'
            return render(request, 'diary_page/diary_update.html', context)

    return render(request, 'diary_page/diary_update.html', context)


#### ---- 포포샵 ---- ####
def shop(request):
    prices = []
    products = Product.objects.all()
    for product in products:
        min_ = 1000000000000
        for i in ProductOption.objects.filter(product=product.id):
            if i.option_price < min_:
                min_ = i.option_price
            prices.append(min_)
    print(prices)
    product = zip(products, prices)
    return render(request, 'shop_page/shop.html', context={'product': product})


def shop_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_option = ProductOption.objects.filter(product=product)

    price = 1000000000000
    for i in product_option:
        if i.option_price < price:
            price = i.option_price
    if request.POST:
        if 'basket_selected' in request.POST:
            basket_selected = eval(request.POST['basket_selected'])

            for i in basket_selected:
                if OrderCount.objects.filter(user=request.user, product_option=ProductOption.objects.get(pk=i)):
                    temp = OrderCount.objects.filter(user=request.user, product_option=ProductOption.objects.get(pk=i))
                    temp.update(order_count_count=basket_selected[i],
                                order_count_price=ProductOption.objects.get(pk=i).option_price * basket_selected[i])
                else:
                    order_count = OrderCount()
                    order_count.user = request.user
                    order_count.product_option = ProductOption.objects.get(pk=i)
                    order_count.order_count_count = basket_selected[i]
                    order_count.order_count_price = ProductOption.objects.get(pk=i).option_price * basket_selected[i]
                    order_count.save()

            products = OrderCount.objects.filter(user=request.user, order_id__isnull=True)
            price = OrderCount.objects.filter(user=request.user).aggregate(Sum('order_count_price'))[
                'order_count_price__sum']
            total_price = price + 2500
            return render(request, 'shop_page/basket.html',
                          context={'products': products, 'price': price, 'total_price': total_price})

    if request.POST:
        if 'buy_selected' in request.POST:
            buy_selected = eval(request.POST['buy_selected'])

            for i in buy_selected:
                if OrderCount.objects.filter(user=request.user, product_option=ProductOption.objects.get(pk=i), order_id__isnull=True):
                    temp = OrderCount.objects.filter(user=request.user, product_option=ProductOption.objects.get(pk=i))
                    temp.update(order_count_count=buy_selected[i],
                                order_count_price=ProductOption.objects.get(pk=i).option_price * buy_selected[i])
                else:
                    order_count = OrderCount()
                    order_count.user = request.user
                    order_count.product_option = ProductOption.objects.get(pk=i)
                    order_count.order_count_count = buy_selected[i]
                    order_count.order_count_price = ProductOption.objects.get(pk=i).option_price * buy_selected[i]
                    order_count.save()
            return payment(request)

    return render(request, 'shop_page/shop_detail.html',
                  context={'product': product, 'product_option': product_option, 'price': price})

@login_required(login_url="/account/")
def payment(request):
    products = OrderCount.objects.filter(user=request.user, order_id__isnull=True)
    price = OrderCount.objects.filter(user=request.user, order_id__isnull=True).aggregate(Sum('order_count_price'))[
        'order_count_price__sum']
    total_price = price
    order_num = Order.objects.all().aggregate(Max('id'))['id__max']+1
    print(order_num)

    if request.POST:
        if 'order_user_name' in request.POST:
            print('여기')
            order_user_name = request.POST['order_user_name']
            order_user_phone_num = request.POST['order_user_phone_num_1'] + '-' + request.POST[
                'order_user_phone_num_2'] + '-' + request.POST['order_user_phone_num_3']
            order_address_num = request.POST['order_address_num']
            order_address = request.POST['order_address_1'] + ' ' + request.POST['order_address_2']
            order_request = request.POST['tec']
            order_price = total_price + 2500

            order = Order()
            order.user = request.user
            order.order_username = order_user_name
            order.order_user_phone_num = order_user_phone_num
            order.order_address_num = order_address_num
            order.order_address = order_address
            order.order_request = order_request
            order.order_price = order_price
            order.save()
            print(order_price)

            OrderCount.objects.filter(user=request.user, order_id__isnull=True).update(order_id=order_num)
            print(order_user_name, order_user_phone_num, order_address_num, order_address, order_request, order_price)
            return order_complete(request, order_num)
    return render(request, 'shop_page/order_payment.html',
                  context={'products': products, 'price': price, 'total_price': total_price, 'order_num': order_num})


def basket_detail(request, context):
    return render(request, 'shop_page/basket.html', context)


def order_complete(request, order_id):
    order_id = order_id
    order = Order.objects.get(id=order_id)
    print(order)
    orders = OrderCount.objects.filter(order_id=order_id)
    print(orders)
    return render(request, 'shop_page/order_complete.html',
                  context={'order_id': order_id, 'orders': orders, 'order': order})


#### ---- 챗봇 ---- ####
def chatbot(request):
    return render(request, 'chatbot_page/chatbot.html', context={})


#### ---- 계정 ---- ####
def account(request):
    return render(request, 'account_page/account.html', context={})


def signup(request):
    # 회원가입 완료 안한 유저
    if User.objects.get(pk=request.user.pk).user_signup_completed == False:
        if request.method == "POST":
            if request.POST['user_signup_completed'] == 'True':
                User.objects.filter(pk=request.user.pk).update(user_nickname=request.POST['user_nickname'],
                                                               user_signup_completed=True)
            if request.FILES:
                user_profile = request.FILES['user_profile']
                userimage = UserImage()
                userimage.user_profile = user_profile
                userimage.user_id = request.user.id
                userimage.save()
                User.objects.filter(pk=request.user.id).update(
                    user_image=UserImage.objects.filter(user_id=request.user.id)[
                        len(UserImage.objects.filter(user_id=request.user.id)) - 1])

            if request.POST['user_email']:
                User.objects.filter(pk=request.user.pk).update(email=request.POST['user_email'])
            return diary_show(request)


    # 회원가입 완료한 유저
    elif User.objects.get(pk=request.user.pk).user_signup_completed == True:
        return diary_show(request)

    return render(request, 'account_page/signup.html', context={})


def board(request):
    diarys = Diary.objects.filter(diary_share_state=True)
    return render(request, 'board_page/board.html', context={'diarys': diarys})


def board_detail(request, diary_id):
    diary_det = get_object_or_404(Diary, pk=diary_id)
    comment_form = CommentForm()
    return render(request, 'board_page/board_detail.html',
                  context={'diary_det': diary_det, 'comment_form': comment_form})


@login_required(login_url="/account/")
def likes(request):
    context = {}
    if request.user.is_authenticated:
        if request.GET['diary_id']:
            current_diary = Diary.objects.get(id=request.GET['diary_id'])
            if current_diary.like_user.filter(pk=request.user.pk).exists():
                current_diary.like_user.remove(request.user)
                context = {'current_diary': current_diary.like_user.count(), 'status': 'False'}
            else:
                current_diary.like_user.add(request.user)
                context = {'current_diary': current_diary.like_user.count(), 'status': 'True'}
            return JsonResponse(context)
    return JsonResponse(context)


#### ---- 고해성사 댓글 ---- ####
def new_comment(request, diary_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.diary = get_object_or_404(Diary, pk=diary_id)
        finished_form.save()
    return redirect('main:board_detail', diary_id)


def mypage(request, user_id):
    context = {}
    user = User.objects.get(pk=user_id)
    context['user'] = user

    return render(request, 'account_page/mypage.html', context)


def uploadProfile(request):
    if request.method == "POST":
        user_profile = request.FILES['user_profile']
        userimage = UserImage()
        userimage.user_profile = user_profile
        userimage.user_id = request.user.id
        userimage.save()
        User.objects.filter(pk=request.user.id).update(user_image=UserImage.objects.filter(user_id=request.user.id)[
            len(UserImage.objects.filter(user_id=request.user.id)) - 1])
        return redirect('main:mypage', request.user.id)
    return diary_show(request)


#### ---- QnA ---- ####
def qna(request):
    qna_list = Qna.objects.all()
    return render(request, template_name='QnA_page/Qna.html', context={'qna_list': qna_list})


@login_required(login_url="/account/")
def qna_create(request):
    if request.method == "POST":
        qna_temp = Qna()
        if request.FILES:
            qna_temp.qna_img = request.FILES['qna_img']

        if request.POST['qna_status'] == 'True':
            qna_temp.qna_status = True

        elif request.POST['qna_status'] == 'False':
            qna_temp.qna_status = False

        qna_temp.user = User.objects.get(pk=request.user.id)
        qna_temp.qna_title = request.POST['qna_title']
        qna_temp.qna_content = request.POST['qna_content']
        qna_temp.save()
        return HttpResponseRedirect(reverse('main:qna'))

    return render(request, 'QnA_page/QnA_create.html')


def qna_detail(request, qna_id):
    qna_detail_object = Qna.objects.get(pk=qna_id)
    return render(request, 'QnA_page/QnA_detail.html', context={'qna_detail_object': qna_detail_object})


def qna_delete(request, qna_id):
    Qna.objects.filter(pk=qna_id).delete()
    return HttpResponseRedirect(reverse('main:qna'))


def qna_update(request, qna_id):
    if request.method == "POST":
        if request.FILES:
            qna_img = request.FILES['qna_img']
            Qna.objects.filter(pk=qna_id).update(qna_img=qna_img)

        if request.POST['qna_status'] == 'True':
            Qna.objects.filter(pk=qna_id).update(qna_status=True)

        elif request.POST['qna_status'] == 'False':
            Qna.objects.filter(pk=qna_id).update(qna_status=False)

        Qna.objects.filter(pk=qna_id).update(qna_title=request.POST['qna_title'],
                                             qna_content=request.POST['qna_content'])
        return qna_detail(request, qna_id)
    qna_detail_object = Qna.objects.get(pk=qna_id)
    return render(request, 'QnA_page/QnA_update.html', context={'qna_detail_object': qna_detail_object})
