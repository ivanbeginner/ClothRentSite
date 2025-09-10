from django.urls import path
from moderation.views import list_moderation_requests
app_name='moderation'

urlpatterns = [
    path('moderation_list',list_moderation_requests,name='moderation_list')
]