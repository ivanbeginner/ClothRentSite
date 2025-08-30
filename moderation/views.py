from django.shortcuts import render, redirect

from moderation.models import ModerationPoster
from posters.forms import PosterAddForm


# Create your views here.

def add_on_moderation(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    form = PosterAddForm(request.POST,request.FILES)
    if request.methos=='POST':
        if form.is_valid():
            data = form.cleaned_data
            poster_moderation = ModerationPoster.objects.create(
                title=data['title'],
                image=data['image'],
                description=data['description'],
            )
