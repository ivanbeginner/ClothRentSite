from django.shortcuts import render, redirect

from posters.forms import PosterAddForm
from posters.models import Poster
from moderation.models import ModerationPoster

# Create your views here.
def list_posters(request):
    posters = Poster.objects.all()
    return render(request,'posters/base.html',{"posters":posters})

def add_poster(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    form = PosterAddForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            data = form.cleaned_data
            moder_add = ModerationPoster.objects.create(
                title=data['title'],
                description=data['description'],
            )
        else:
            form = PosterAddForm()
    return render(request,'posters/create_poster.html',{'form':form})