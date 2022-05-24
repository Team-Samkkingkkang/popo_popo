from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_nickname = models.CharField(max_length=200)
    user_profile = models.ImageField(null=True)
    user_regi_date = models.DateTimeField(auto_now_add=True)
    user_number = models.IntegerField(null=True)
    user_auth_type = models.BooleanField(null=True)
    user_address_number = models.CharField(max_length=200)
    user_address = models.CharField(max_length=200)
    user_delivery_number = models.IntegerField(null=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_number = models.IntegerField()
    order_price = models.IntegerField()
    order_delivery_fee = models.IntegerField()
    order_username = models.CharField(max_length=200)
    order_user_phone_num = models.CharField(max_length=200)
    order_address_num = models.CharField(max_length=200)
    order_request = models.TextField()
    order_agree = models.BooleanField()


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_info = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_emotion = models.CharField(max_length=200)


class Qna(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qna_title = models.CharField(max_length=200)
    qna_content = models.TextField()
    qna_date = models.DateTimeField(auto_now=True)
    qna_img = models.ImageField()
    qna_status = models.BooleanField()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket_price = models.IntegerField()
    basket_delivery_fee = models.IntegerField()


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option_classification = models.TextField()
    option_name = models.CharField(max_length=200)
    option_price = models.IntegerField()


class OrderCount(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    order_count_count = models.IntegerField()
    order_count_price = models.IntegerField()


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    diary_content = models.TextField()
    diary_date = models.DateTimeField(auto_now_add=True)
    diary_img = models.ImageField(upload_to='diary_img/', null=True, blank=True)
    diary_share_state = models.BooleanField(default=False)


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


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)