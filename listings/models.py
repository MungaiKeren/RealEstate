from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    main_image = models.ImageField(upload_to="photos/%Y/%m/%d")
    image_1 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    image_2 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    image_3 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    image_4 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    image_5 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    image_6 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.title

