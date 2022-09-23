from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'anons', 'full_text', 'date']

        widgets = {
            'name': TextInput(attrs= {
                'class':'form-control',
                'placeholder':'Имя'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст отзыва'
            }),

        }