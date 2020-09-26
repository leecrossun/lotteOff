from django.db import models

class Products(models.Model):
    storeName = models.CharField(max_length=20)
    p_name = models.CharField(max_length=20)
    p_image = models.ImageField(upload_to='images/')
    p_price = models.IntegerField(default=0)
    p_sold_out = models.BooleanField(default=False)
    p_info = models.TextField()

    def __str__(self):
        return self.storeName

