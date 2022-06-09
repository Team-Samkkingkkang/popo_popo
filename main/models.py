from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import datetime
import datetime

from config import settings


class UserImage(models.Model):
    user_profile = models.ImageField(default='default_img/diary_default_img.png', upload_to='profile_img/', null=True,
                                     blank=True)
    user_id = models.IntegerField(null=True)


class User(AbstractUser):
    user_nickname = models.CharField(max_length=200, unique=False)  # 따로 설정 필요
    user_regi_date = models.DateTimeField(auto_now_add=True)
    user_auth_type = models.BooleanField(default=False)
    user_signup_completed = models.BooleanField(default=False)
    user_image = models.ForeignKey(UserImage, on_delete=models.SET_NULL, null=True)
    # + email 필드 사용


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_price = models.IntegerField()
    order_user_name = models.CharField(max_length=200)
    order_user_phone_num = models.CharField(max_length=200)
    order_address_num = models.CharField(max_length=200)
    order_address = models.CharField(max_length=200)
    order_request = models.TextField()


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_info = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_emotion = models.CharField(max_length=200)
    product_img = models.ImageField(null=True, upload_to='product_img/')



class Qna(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qna_title = models.CharField(max_length=200)
    qna_content = models.TextField()
    qna_date = models.DateTimeField(auto_now=True)
    qna_img = models.ImageField(null=True, blank=True)
    qna_status = models.BooleanField()


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option_classification = models.TextField()
    option_name = models.CharField(max_length=200)
    option_price = models.IntegerField()


class OrderCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    order_count_count = models.IntegerField()
    order_count_price = models.IntegerField()


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    diary_content = models.TextField()
    diary_date = models.DateTimeField(auto_now_add=True)
    diary_img = models.ImageField(upload_to='diary_img/', null=True, blank=True, default='default_img/paper.jpg')
    diary_share_state = models.BooleanField(default=False)
    diary_share_date = models.DateTimeField(auto_now_add=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_diary')


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    board_title = models.CharField(max_length=200)
    board_content = models.TextField()
    board_date = models.DateTimeField()
    board_img = models.ImageField()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment_content = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)
