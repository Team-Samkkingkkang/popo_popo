# Generated by Django 4.0.4 on 2022-06-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_diary_diary_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_address_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_delivery_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_auth_type',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.ImageField(default='default_img/diary_default_img.png', upload_to=''),
        ),
    ]
