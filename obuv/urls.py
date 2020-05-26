from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:pk>/', views.product_view, name='product_view'),
    path('about_us/', views.about_us, name='about_us'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:pk>/', views.articles_view, name='article_view'),
    path('contacts/', views.contacts, name='contacts'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns += staticfiles_urlpatterns()
