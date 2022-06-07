from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from main import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'main'


urlpatterns = [
    # 메인 화면
    path('', TemplateView.as_view(template_name='base.html'), name='main'),

    # 다이어리
    path('diary/', views.diary, name="diary"),
    path('diary_create/', views.diary_create, name="diary_create"),
    path('diary_show/', views.diary_show, name="diary_show"),
    path('diary_show/share_status', views.share_status, name="share_status"),
    path('diary_detail/', views.diary_detail, name="diary_detail"),
    path('diary_delete/<int:diary_id>/', views.diary_delete, name="diary_delete"),
    path('diary_update/<int:diary_id>/', views.diary_update, name="diary_update"),

    # 포포샵
    path('shop/', views.shop, name="shop"),

    # 챗봇
    path('chatbot/', views.chatbot, name="chatbot"),

    # 계정
    path('account/', views.account, name="account"),
    path('account/signup/', views.signup, name="signup"),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 게시판
    path('board/', views.board, name="board"),
    path('board_detail/<int:diary_id>/', views.board_detail, name="board_detail"),
    path('<int:diary_id>/likes/', views.likes, name='likes'),
    path('mypage/<int:user_id>/', views.mypage, name="mypage"),
    path('uploadProfile/', views.uploadProfile, name="uploadProfile"),

    # 댓글
    # path('comment/<int:diary_id>', views.comment, name='comment'),
    path('new_comment/<int:diary_id>/', views.new_comment, name="new_comment")
]

