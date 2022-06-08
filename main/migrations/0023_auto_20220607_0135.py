# Generated by Django 3.2.13 on 2022-06-06 16:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_user_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='like_user',
            field=models.ManyToManyField(related_name='like_diary', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
