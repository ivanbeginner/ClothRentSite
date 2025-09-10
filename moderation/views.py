from django.shortcuts import render, redirect
from django.contrib import messages
from moderation.models import ModerationPoster
from posters.forms import PosterAddForm


# Create your views here.

def list_moderation_requests(request):
    if not request.user.is_staff:
        messages.error(request,'Недостаточно прав')
    lst = ModerationPoster.objects.all()
    return render(request,'moderation/list_requests.html',{'list',lst})

def approve_request(request,moderation_poster_id):
    if not request.user.is_staff:
        messages.error(request,'Недостаточно прав')
    update = ModerationPoster.objects.filter(pk=moderation_poster_id).update(is_approved=True)
    return redirect('moderation:moderation_list')

