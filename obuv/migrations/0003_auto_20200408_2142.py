# Generated by Django 3.0.5 on 2020-04-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obuv', '0002_auto_20200408_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banners', verbose_name='Изображение'),
        ),
    ]
