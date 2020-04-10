# Generated by Django 3.0.5 on 2020-04-09 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obuv', '0008_auto_20200409_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verh',
            options={'verbose_name': 'Материал верха', 'verbose_name_plural': 'Верх, матриалы'},
        ),
        migrations.AddField(
            model_name='banner',
            name='link',
            field=models.URLField(default=None, verbose_name='Ссылка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='podoshva',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Материал подошвы'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='obuv.Color', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='genre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='obuv.Genre', verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='product',
            name='podkladka',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='obuv.Podkladka', verbose_name='Подкладка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='podoshva',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='obuv.Podoshva', verbose_name='Подошва'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='obuv.Size', verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='obuv.Type', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='product',
            name='verh',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='obuv.Verh', verbose_name='Верх'),
        ),
    ]
