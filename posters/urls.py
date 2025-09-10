from django.urls import path
from posters.views import add_poster,list_posters
app_name='posters'

urlpatterns = [
    path('',list_posters,name='list_posters'),
    path('add_req_mod/',add_poster,name='add_req_mod')
]
