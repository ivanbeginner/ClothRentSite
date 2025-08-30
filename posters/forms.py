from django import forms

from posters.models import Category

categories = Category.objects.all()
choices = ((category.pk,category.name) for category in categories)
class PosterAddForm(forms.Form):
    title = forms.CharField()
    image = forms.FileField()
    description = forms.CharField()
    price = forms.IntegerField(min_value=0)
    location = forms.CharField()
    contacts = forms.CharField()
    date_start_rent = forms.DateTimeField(widget=forms.DateTimeInput)
    date_ens_rent = forms.DateTimeField(widget=forms.DateTimeInput)
    category = forms.ChoiceField(choices=choices)