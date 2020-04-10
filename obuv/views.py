from django.shortcuts import render
from .models import Banner, Product


def index(request):
    banners = Banner.objects.all()
    products = Product.objects.all()
    title = 'Производство обуви'
    description = 'Бла Бла Бла'
    return render(request, 'index.html', {'title': title, 'banners': banners, 'description': description,
                                          'products': products})
