# Generated by Django 3.0.5 on 2020-04-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obuv', '0016_auto_20200424_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_page',
            field=models.BooleanField(default=False, verbose_name='Виден на главной'),
        ),
    ]