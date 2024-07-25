from django.db import models

class Course(models.Model):
    name = models.CharField('Название', max_length=255)
    language = models.CharField('Язык', max_length=15)
    version = models.CharField('Версия', max_length=15)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    description = models.TextField('Описание')
    recommended = models.TextField('Рекомендовано')
    date = models.DateTimeField('Создан')
    lessons = models.PositiveSmallIntegerField('Количество уроков')
    tasks = models.TextField('Задания (формат данных уточняется)')
    favorites = models.PositiveIntegerField('Добавлено в избранное')
    purchased = models.PositiveIntegerField('Количество покупок')
    passed = models.PositiveIntegerField('Выдано сертификатов')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/course/{self.id}'
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
