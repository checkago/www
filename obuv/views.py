from django.shortcuts import render

def index(request):
    title = 'Производство обуви'
    description = ''
    return render(request, 'index.html', title)
