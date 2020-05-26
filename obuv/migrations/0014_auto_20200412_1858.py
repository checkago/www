# Generated by Django 3.0.5 on 2020-04-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obuv', '0013_auto_20200412_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, upload_to='catalog/products', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to='catalog/products', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to='catalog/products', verbose_name='Изображение'),
        ),
    ]