from django.shortcuts import render


# Create your views here.

def diary(request):
    return render(request, 'diary_page/diary.html', context={})


def shop(request):
    return render(request, 'shop_page/shop.html', context={})


def chatbot(request):
    return render(request, 'chatbot_page/chatbot.html', context={})


def account(request):
    return render(request, 'account_page/account.html', context={})
