# Generated by Django 3.0.5 on 2020-05-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obuv', '0024_minibanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='minibanner',
            name='image',
            field=models.ImageField(blank=True, upload_to='minibanners', verbose_name='Изображение'),
        ),
    ]
