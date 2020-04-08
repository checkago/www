from django.shortcuts import render
from .models import Banner


def index(request):
    banners = Banner.objects.all()
    title = 'Производство обуви'
    description = ''
    return render(request, 'index.html', {title:'title', banners:'banners', description:'description'})
