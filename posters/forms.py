from django import forms

from posters.models import Category

categories = Category.objects.all()
choices = ((category.name,category.name) for category in categories)
class PosterAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False
    title = forms.CharField(label='Название')
    image = forms.FileField(label='Изображение')
    description = forms.CharField(label='Описание')
    price = forms.IntegerField(min_value=0,label='Цена')
    location = forms.CharField(label='Адрес')
    contacts = forms.CharField(label='Контакты')
    date_start_rent = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}),label='Начало аренды')
    date_ens_rent = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}),label='Конец аренды')
    category = forms.ChoiceField(choices=choices,label='Категория')