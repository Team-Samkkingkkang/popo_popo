# Generated by Django 3.2.13 on 2022-06-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_user_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_img',
            field=models.ImageField(blank=True, null=True, upload_to='user_img'),
        ),
    ]
