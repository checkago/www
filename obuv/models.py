from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    anons = models.TextField(verbose_name='Анонс')
    link = models.URLField(verbose_name='Ссылка', blank=True)
    image = models.ImageField(upload_to='banners', verbose_name='Изображение')
    public = models.BooleanField(default=False, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Принадлежность')

    class Meta:
        verbose_name = 'Пол'

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип обуви')

    class Meta:
        verbose_name = 'Вид обуви'
        verbose_name_plural = 'Виды обуви'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=3, verbose_name='Размер')
    genre = models.ForeignKey('Genre', on_delete=models.DO_NOTHING, verbose_name='genre_size')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Verh(models.Model):
    name = models.CharField(max_length=100, verbose_name='Материал верха')

    class Meta:
        verbose_name = 'Материал верха'
        verbose_name_plural = 'Верх, матриалы'

    def __str__(self):
        return self.name


class Podkladka(models.Model):
    name = models.CharField(max_length=100, verbose_name='Материал подкладки')

    class Meta:
        verbose_name  ='Материал подкладки'
        verbose_name_plural = 'Материал подкладок'

    def __str__(self):
        return self.name


class Podoshva(models.Model):
    name = models.CharField(max_length=50, verbose_name='Материал подошвы')

    class Meta:
        verbose_name = 'Материал подошвы'
        verbose_name_plural = 'Материалы подошв'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    article = models.CharField(max_length=10, verbose_name='Артикул', blank=True)
    type = models.ForeignKey('Type', on_delete=models.DO_NOTHING, blank=True, verbose_name='Тип')
    color = models.ForeignKey('Color', on_delete=models.DO_NOTHING, blank=True, verbose_name='Цвет')
    genre = models.ForeignKey('Genre', on_delete=models.DO_NOTHING, blank=True, verbose_name='Пол')
    size = models.ForeignKey('Size', on_delete=models.DO_NOTHING, blank=True, verbose_name='Размер')
    verh = models.ForeignKey('Verh', on_delete=models.DO_NOTHING, blank=True, verbose_name='Верх')
    podkladka = models.ForeignKey('Podkladka', on_delete=models.DO_NOTHING, blank=True, verbose_name='Подкладка')
    podoshva = models.ForeignKey('Podoshva', on_delete=models.DO_NOTHING, blank=True, verbose_name='Подошва')

    class Meta:
        verbose_name = 'Обувной товар'
        verbose_name_plural = 'Обувные товары'

    def __str__(self):
        return self.name
