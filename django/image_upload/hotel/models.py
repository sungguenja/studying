from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    hotel_main_Img = models.ImageField(upload_to='images/')