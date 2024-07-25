from django.forms import ModelForm, TextInput, Textarea
from .models import Language

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = [
            'name',
            'version',
            'icon',
            'tiobe',
            'typing',
            'translation',
            'product',
            'usage',
            'editor',
            'description',
            'trend',
            'example'
        ]
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Название языка'}),
            'version': TextInput(attrs={'placeholder': 'Текущая версия'}),
            'icon': TextInput(attrs={'type': 'file', 'name': "upload", 'placeholder': 'Иконка'}),
            'tiobe': TextInput(attrs={'placeholder': 'Рейтинг TIOBE'}),
            'typing': TextInput(attrs={'placeholder': 'Типизация'}),
            'translation': TextInput(attrs={'placeholder': 'Трансляция'}),
            'product': TextInput(attrs={'placeholder': 'Популярные программы'}),
            'usage': TextInput(attrs={'placeholder': 'Фреймворки и т.д.'}),
            'editor': TextInput(attrs={'placeholder': 'Редактор'}),
            'description': Textarea(attrs={'placeholder': 'Описание'}),
            'trend': Textarea(attrs={'placeholder': 'Область применения'}),
            'example': Textarea(attrs={'placeholder': 'Пример кода'})
        }
