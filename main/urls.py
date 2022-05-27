from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from main import views

app_name = 'main'

urlpatterns = [
    # 메인 화면
    path('', TemplateView.as_view(template_name='base.html'), name='main'),

    # 다이어리
    path('diary/', views.diary, name="diary"),
    path('diary_create/', views.diary_create, name="diary_create"),
    path('diary_show/', views.diary_show, name="diary_show"),
    path('diary_detail/<int:diary_id>/', views.diary_detail, name="diary_detail"),
    path('diary_delete/<int:diary_id>/', views.diary_delete, name="diary_delete"),
    path('diary_update/<int:diary_id>/', views.diary_update, name="diary_update"),
path('diary_detail/<int:diary_id>/', views.diary_detail, name="diary_detail"),

    # 포포샵
    path('shop/', views.shop, name="shop"),

    # 챗봇
    path('chatbot/', views.chatbot, name="chatbot"),

    # 계정
    path('account/', views.account, name="account"),

    # 게시판
    path('board/', views.board, name="board"),

]
