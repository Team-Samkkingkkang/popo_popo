from django.contrib import admin

# Register your models here.
from main.models import Diary, Product, ProductOption


admin.site.register(Diary)

admin.site.register(Product)

admin.site.register(ProductOption)