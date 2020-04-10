from django.contrib import admin
from obuv.models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'anons', 'public')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre',)


class VerhAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PodkladkaAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PodoshvaAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'genre', 'name', 'color', 'size', 'article',)


admin.site.register(Banner, BannerAdmin),
admin.site.register(Genre, GenreAdmin),
admin.site.register(Type, TypeAdmin),
admin.site.register(Color, ColorAdmin),
admin.site.register(Size, SizeAdmin),
admin.site.register(Verh, VerhAdmin),
admin.site.register(Podkladka, PodkladkaAdmin),
admin.site.register(Podoshva, PodoshvaAdmin),
admin.site.register(Product, ProductAdmin),

