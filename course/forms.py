from django.forms import ModelForm, TextInput, Textarea
from .models import Course

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'language',
            'version',
            'description',
            'recommended',
            'date',
            'lessons',
            'tasks',
            'price',
            'favorites',
            'purchased',
            'passed'
        ]
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Название курса'}),
            'language': TextInput(attrs={'placeholder': 'Название'}),
            'version': TextInput(attrs={'placeholder': 'Версия'}),
            'description': TextInput(attrs={'placeholder': 'Описание'}),
            'recommended': TextInput(attrs={'placeholder': 'Рекомендовано'}),
            'date': TextInput(attrs={'placeholder': 'Создан'}),
            'lessons': TextInput(attrs={'placeholder': 'Количество уроков'}),
            'tasks': TextInput(attrs={'placeholder': 'Задания (формат данных уточняется)'}),
            'price': TextInput(attrs={'placeholder': 'Цена'}),
            'favorites': TextInput(attrs={'placeholder': 'Добавлено в избранное'}),
            'purchased': TextInput(attrs={'placeholder': 'Количество покупок'}),
            'passed': TextInput(attrs={'placeholder': 'Выдано сертификатов'})
        }
