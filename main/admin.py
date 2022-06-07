from django.contrib import admin

# Register your models here.
from main.models import Diary

from main.models import User

admin.site.register(Diary)

admin.site.register(User)