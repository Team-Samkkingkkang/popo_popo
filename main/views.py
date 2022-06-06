from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
# Create your views here.

#### ---- 다이어리 ---- ####
from main.models import Diary, User


def diary(request):
    return render(request, 'diary_page/diary.html', context={})


def diary_create(request):
    if request.method == 'POST':

        diary_model = Diary()
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


def diary_show(request):
    diarys = Diary.objects.all()
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
    return render(request, 'shop_page/shop.html', context={})


#### ---- 챗봇 ---- ####
def chatbot(request):
    return render(request, 'chatbot_page/chatbot.html', context={})


#### ---- 계정 ---- ####
def account(request):
    return render(request, 'account_page/account.html', context={})


def signup(request):
    # 회원가입 완료 안한 유저
    if User.objects.get(pk=request.user.pk).user_signup_completed == True:
        if request.method == "POST":
            if request.POST['user_signup_completed'] == 'True':
                User.objects.filter(pk=request.user.pk).update(user_nickname=request.POST['user_nickname'],
                                                               user_signup_completed=True)
            if request.FILES['user_profile']:
                user_profile = request.FILES['user_profile']
                User.objects.filter(pk=request.user.pk).update(user_profile=user_profile)

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


def mypage(request, user_id):
    context = {}
    user = User.objects.get(pk=user_id)
    context['user'] = user

    if request.method == 'POST':
        if request.FILES:
            user_profile = request.FILES['user_profile']
            User.objects.get(pk=user_id).update(user_profile=user_profile)
        else:
            return 0;

    return render(request, 'account_page/mypage.html', context)
