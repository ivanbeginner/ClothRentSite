from django.contrib import admin

from posters.models import Poster, Category


# Register your models here.
@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ['author','title','description','price','location','contacts','date_start_rent','date_end_rent','category']

@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display = ['name']

