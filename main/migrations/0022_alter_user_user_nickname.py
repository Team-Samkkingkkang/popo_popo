# Generated by Django 3.2.13 on 2022-06-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_user_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_nickname',
            field=models.CharField(max_length=200),
        ),
    ]
