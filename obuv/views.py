from django.shortcuts import render, get_object_or_404
from .models import Banner, Product, Partner, Article, Minibanner, About


def index(request):
    banners = Banner.objects.all()
    products = Product.objects.order_by('?')
    minibanners = Minibanner.objects.all()
    partners = Partner.objects.all()
    articles = Article.objects.all()
    title = 'ЭРА-РА | Производство обуви'
    description = 'Бла Бла Бла'
    return render(request, 'index/index.html', {'title': title, 'banners': banners, 'description': description,
                                                'products': products, 'partners': partners, 'articles': articles,
                                                'minibanners': minibanners})


def catalog(request):
    products = Product.objects.order_by('?')
    genre = Product.genre
    title = 'Каталог обуви ЭРА-РА'
    description = 'Каталог обуви производства ООО "ВОСХОД" под брендом ЭРА-РА и ЭКО-СПОРТ'
    return  render(request, 'catalog/catalog.html', {'title': title, 'description': description, 'products': products, 'genre': genre})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    name = Product.name
    article = Product.article
    type = Product.type
    genre = Product.genre
    color = Product.color
    size = Product.size
    verh = Product.verh
    podkladka = Product.podkladka
    podoshva = Product.podoshva
    product_related = Product.objects.all()
    return  render(request, 'catalog/product_details.html', {'product': product, 'name': name, 'article': article,
                                                             'type': type, 'genre': genre, 'color': color, 'size': size,
                                                             'verh': verh, 'podkladka': podkladka,
                                                             'podoshva': podoshva, 'product_related': product_related,})


def articles(request):
    articles = Article.objects.all()
    title = 'Статьи и анонсы'
    minibanners = Minibanner.objects.all()
    description = 'Статьи о производстве и продукции фирмы ООО "Восход", производителе повседневной обуви'
    return render(request, 'articles/articles.html', {'title': title, 'description': description, 'articles': articles,
                                                      'minibanners': minibanners,})


def articles_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    description = Article.short_text
    minibanner = Minibanner.objects.all()
    return render(request, 'articles/article_detail.html', {'article': article, 'description': description,
                                                            'minibanner': minibanner,})


def about_us(request):
    title = 'О компании ООО "ВОСХОД"'
    description = 'Производитель повседневной обуви для ...'
    abouts = About.objects.all()
    partners = Partner.objects.all()
    return render(request, 'about_us.html', {'title': title, 'description': description, 'abouts': abouts, 'partners': partners,})


def contacts(request):
    title = 'Контакты'
    description = 'Наши контакты | ООО "ВОСХОД"'
    return render(request, 'contacts.html', {'title': title, 'description': description})