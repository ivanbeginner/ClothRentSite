from django.shortcuts import render, redirect

from posters.forms import PosterAddForm
from posters.models import Poster


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
            poster = Poster.objects.create(
                title=data['title'],
                description=data['description'],
                price=data['price'],
                location=data['location'],
                contacts=data['contacts'],
                date_start_rent=data['date_start_rent'],
                date_end_rent=data['date_end_rent'],
                categoty=data['category']
            )
        else:
            form = PosterAddForm()
    return render(request,'posters/create_poster.html',{'form':form})