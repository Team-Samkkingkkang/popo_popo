from django.contrib import admin
from django.urls import path, include

from main import views

app_name = 'main'

urlpatterns = [
    path('diary/', views.diary, name="diary"),
    path('shop/', views.shop, name="shop"),
    path('chatbot/', views.chatbot, name="chatbot"),
    path('account/', views.account, name="account"),

]
