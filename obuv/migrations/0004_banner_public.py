# Generated by Django 3.0.5 on 2020-04-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obuv', '0003_auto_20200408_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
