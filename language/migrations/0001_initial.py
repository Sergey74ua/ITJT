# Generated by Django 5.0.7 on 2024-07-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True, verbose_name='Название')),
                ('version', models.CharField(default='не установлена', max_length=15, verbose_name='Версия')),
                ('icon', models.FileField(default='не загружена', upload_to='', verbose_name='Иконка')),
                ('tiobe', models.DecimalField(decimal_places=3, default='0', max_digits=5, verbose_name='Индекс TIOBE')),
                ('typing', models.TextField(default='не описана', verbose_name='Типизация')),
                ('translation', models.TextField(default='не описана', verbose_name='Трансляция')),
                ('product', models.TextField(default='не указаны', verbose_name='Продукты')),
                ('usage', models.TextField(default='не указаны', verbose_name='Реализация')),
                ('editor', models.TextField(default='не указаны', verbose_name='Редактор')),
                ('description', models.TextField(default='не указано', verbose_name='Описание')),
                ('trend', models.TextField(default='не указано', verbose_name='Применение')),
                ('example', models.TextField(default='отсутствует', verbose_name='Пример')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
    ]
