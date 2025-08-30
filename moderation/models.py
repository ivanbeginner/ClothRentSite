from django.db import models

# Create your models here.
class ModerationPoster(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)