# Generated by Django 4.0.4 on 2022-06-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_merge_20220609_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(null=True, upload_to='product_img/'),
        ),
    ]
