from django.db import models
from datetime import date
from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(null=False,unique=True)
    def __str__(self):
        return self.name
class Poster(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(null=False,max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    price = models.PositiveIntegerField(null=False,default=0)
    location = models.CharField(null=False)
    contacts = models.CharField(default='')
    date_start_rent = models.DateTimeField(auto_now_add=True)
    date_end_rent = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)



