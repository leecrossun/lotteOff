from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class NewProduct(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'image/')
    image_thumnail = ImageSpecField(source='image', processors=[ResizeToFill(150, 100)])

    def __str__(self):
        return self.title