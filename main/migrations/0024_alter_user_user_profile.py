# Generated by Django 3.2.13 on 2022-06-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20220607_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.ImageField(blank=True, default='default_img/diary_default_img.png', null=True, upload_to='profile_img/'),
        ),
    ]
