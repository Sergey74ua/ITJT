from django.db import models

class Language(models.Model):
    name = models.CharField('Название', max_length=15)
    version = models.CharField('Версия', max_length=15)
    icon = models.FileField('Иконка')
    tiobe = models.DecimalField('Индекс TIOBE', max_digits=5, decimal_places=3)
    typing = models.TextField('Типизация')
    translation = models.TextField('Трансляция')
    product = models.TextField('Продукты')
    usage = models.TextField('Реализация')
    editor = models.TextField('Редактор')
    description = models.TextField('Описание')
    trend = models.TextField('Применение')
    example = models.TextField('Пример')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/language/{self.id}'

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
