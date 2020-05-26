# Generated by Django 3.0.5 on 2020-05-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obuv', '0022_auto_20200505_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=100, verbose_name='Название ссылки')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок статьи')),
                ('short_text', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('image', models.ImageField(blank=True, upload_to='articles', verbose_name='Изображение статьи')),
                ('full_text', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('main_page', models.BooleanField(default=False, verbose_name='Публиковать на главной')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]