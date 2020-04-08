from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    anons = models.TextField(verbose_name='Анонс')
    image = models.ImageField(upload_to='media/banners')
    def meta(self):
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'