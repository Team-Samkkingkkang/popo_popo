# Generated by Django 4.0.4 on 2022-05-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_diary_diary_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_img',
            field=models.ImageField(blank=True, default='default_img/paper.jpg', null=True, upload_to='diary_img/'),
        ),
    ]
