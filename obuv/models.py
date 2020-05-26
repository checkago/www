from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок')
    anons = models.TextField(blank=True, verbose_name='Анонс')
    link = models.URLField(verbose_name='Ссылка', blank=True)
    image = models.ImageField(upload_to='banners', verbose_name='Изображение')
    position = models.CharField(max_length=1, verbose_name='Очередность вывода')
    public = models.BooleanField(default=False, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.name


class Minibanner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название минибаннера')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    image = models.ImageField(upload_to='minibanners', blank=True, verbose_name='Изображение')
    text = models.TextField(blank=True, verbose_name='Текст баннера')
    link = models.URLField(blank=True, verbose_name='сслыка на публикацию')
    main_page = models.BooleanField(default=False, verbose_name='Опубликлован на главной')
    public_all = models.BooleanField(default=False, verbose_name='Опубликован в блоке анонсов')

    class Meta:
        verbose_name = 'Минибаннер на главной'
        verbose_name_plural = 'Минибаннеры'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_sizes(self):
        return self.sizes.filter(genre=self)

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
    genre = models.ForeignKey('Genre', on_delete=models.DO_NOTHING, related_name='sizes', verbose_name='Принадлежность')

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
        verbose_name = 'Материал подкладки'
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


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Партнеры')
    brend_logo = models.ImageField(upload_to='partners', blank=True, verbose_name='Лого партнера')
    link = models.URLField(verbose_name='Ссылка на сайт партнера', blank=True)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    article = models.CharField(max_length=10, verbose_name='Артикул', blank=True)
    type = models.ForeignKey('Type', on_delete=models.DO_NOTHING, blank=True, verbose_name='Тип')
    color = models.ForeignKey('Color', on_delete=models.DO_NOTHING, blank=True, verbose_name='Цвет')
    genre = models.ForeignKey('Genre', on_delete=models.DO_NOTHING, blank=True, verbose_name='Пол')
    size = models.ManyToManyField('Size', blank=True, verbose_name='Размер')
    verh = models.ForeignKey('Verh', on_delete=models.DO_NOTHING, blank=True, verbose_name='Верх')
    podkladka = models.ForeignKey('Podkladka', on_delete=models.DO_NOTHING, blank=True, verbose_name='Подкладка')
    podoshva = models.ForeignKey('Podoshva', on_delete=models.DO_NOTHING, blank=True, verbose_name='Подошва')
    description = models.TextField(blank=True, verbose_name='Описание')
    image1 = models.ImageField(upload_to='catalog/products', blank=True, verbose_name='Изображение 1')
    image2 = models.ImageField(upload_to='catalog/products', blank=True, verbose_name='Изображение 2')
    image3 = models.ImageField(upload_to='catalog/products', blank=True, verbose_name='Изображение 3')
    image4 = models.ImageField(upload_to='catalog/products', blank=True, verbose_name='Изображение 4')
    image5 = models.ImageField(upload_to='catalog/products', blank=True, verbose_name='Изображение 5')
    main_page = models.BooleanField(default=False, verbose_name='Виден на главной в продукции')
    top_sale = models.BooleanField(default=False, verbose_name='Виден в топ продаж')
    catalog_in = models.BooleanField(default=True, verbose_name='Присутствует в каталоге')

    class Meta:
        verbose_name = 'Обувной товар'
        verbose_name_plural = 'Обувные товары'

    def __str__(self):
        return self.name


class Article(models.Model):
    slug = models.CharField(max_length=100, blank=True, verbose_name='Название ссылки')
    art_title = models.CharField(max_length=150, verbose_name='Заголовок статьи')
    short_text = models.TextField(blank=True, verbose_name='Краткое описание')
    thumbnail = models.ImageField(upload_to='articles', blank=True, verbose_name='Изображение на главной')
    image = models.ImageField(upload_to='articles', blank=True, verbose_name='Изображение статьи')
    full_text = models.TextField(blank=True, verbose_name='Текст статьи')
    main_page = models.BooleanField(default=False, verbose_name='Публиковать на главной')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.art_title


class Proizvodstvo(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    adress = models.CharField(max_length=250, blank=True, verbose_name='Адрес склада/производства')
    phone = models.CharField(max_length=18, blank=True, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Производсто/Склад'
        verbose_name_plural = 'Производства/Склады'

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название компании')
    yur_adress = models.CharField(max_length=300, blank=True, verbose_name='Юридический адрес')
    inn = models.CharField(max_length=10, blank=True, verbose_name='ИНН')
    date = models.DateField(blank=True, verbose_name='Дата регистрации')
    image = models.ImageField(upload_to='about_us', verbose_name='Основноре фото', blank=True)
    text1 = models.TextField(verbose_name='Первая часть текста')
    image1 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Изображение 1_1')
    image2 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Изображение 1_2')
    image3 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Изображение 1_3')
    text2 = models.TextField(verbose_name='Вторая часть текста')
    image4 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Изображение 2_1')
    image5 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Изображение 2_2')
    image6 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Изображение 2_3')
    proizvodstva = models.ManyToManyField('Proizvodstvo', blank=True, verbose_name='Склады и производства')
    text3 = models.TextField(blank=True, verbose_name='Третья часть текста')
    image7 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Изображение 3_1')
    image8 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Изображение 3_2')
    cert_image1 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Сертификат 1')
    cert_file1 = models.FileField(upload_to='about_us', blank=True, verbose_name='Файл серификата 1')
    cert_image2 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Сертификат 2')
    cert_file2 = models.FileField(upload_to='about_us', blank=True, verbose_name='Файл серификата 2')
    cert_image3 = models.ImageField(upload_to='about_us', blank=True, verbose_name='Сертификат 3')
    cert_file3 = models.FileField(upload_to='about_us', blank=True, verbose_name='Файл серификата 3')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


