from django.shortcuts import render

# Create your views here.

#### ---- 다이어리 ---- ####
from main.models import Diary


def diary(request):
    return render(request, 'diary_page/diary.html', context={})


def diary_create(request):
    if request.method == 'POST':
        if request.POST.get('diary_img') or request.POST.get('diary_content'):
            diary_img = request.POST.get('diary_img')
            diary_content = request.POST.get('diary_content')

            diary_model = Diary()
            diary_model.diary_img = diary_img
            diary_model.diary_content = diary_content
            diary_model.save()
        return render(request, 'diary_page/diary.html', context={})
    return render(request, 'diary_page/diary_create.html', context={})


def diary_show(request):
    return render(request, 'diary_page/diary_show.html', context={})


def diary_update(request):
    return render(request, 'diary_page/diary_update.html', context={})


#### ---- 포포샵 ---- ####
def shop(request):
    return render(request, 'shop_page/shop.html', context={})


#### ---- 챗봇 ---- ####
def chatbot(request):
    return render(request, 'chatbot_page/chatbot.html', context={})


#### ---- 계정 ---- ####
def account(request):
    return render(request, 'account_page/account.html', context={})


def board(request):
    return render(request, 'board_page/board.html', context={})
