from django.contrib import admin

from posters.models import Poster, Category


# Register your models here.


class CategoryAmin(admin.ModelAdmin):
    list_display = ['name']
class PosterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Poster._meta.get_fields()]
    
    
    
    

admin.site.register(Category,CategoryAmin)
admin.site.register(Poster,PosterAdmin)
