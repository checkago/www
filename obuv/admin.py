from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from obuv.models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'title', 'anons', 'public')


class MinibannerAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))

    class Meta:
        model = Minibanner
        fields = '__all__'


class MinibannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'main_page', 'public_all',)


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


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'link',)


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'genre', 'name', 'color', 'article',)
    form = ProductAdminForm


class ArticleAdminForm(forms.ModelForm):
    short_text = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
    full_text = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'art_title', 'main_page',)
    form = ArticleAdminForm


class AboutAdminForm(forms.ModelForm):
    text1 = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
    text2 = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
    text3 = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))

    class Meta:
        model = About
        fields = '__all__'


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn',)
    form = AboutAdminForm


class ProizvodstvoAdmin(admin.ModelAdmin):
    list_display = ('name', 'adress',)


admin.site.register(Banner, BannerAdmin),
admin.site.register(Minibanner, MinibannerAdmin)
admin.site.register(Genre, GenreAdmin),
admin.site.register(Type, TypeAdmin),
admin.site.register(Color, ColorAdmin),
admin.site.register(Size, SizeAdmin),
admin.site.register(Verh, VerhAdmin),
admin.site.register(Podkladka, PodkladkaAdmin),
admin.site.register(Podoshva, PodoshvaAdmin),
admin.site.register(Partner, PartnerAdmin),
admin.site.register(Product, ProductAdmin),
admin.site.register(Article, ArticleAdmin),
admin.site.register(About, AboutAdmin),
admin.site.register(Proizvodstvo, ProizvodstvoAdmin),

