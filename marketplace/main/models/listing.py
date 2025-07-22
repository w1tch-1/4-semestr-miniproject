from django.db import models
from main.choices import PriceTypeChoices


class Listing(models.Model):
    category = models.ForeignKey('main.Category', related_name='products', on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey('main.SubCategory', related_name='products', on_delete=models.SET_NULL, null=True)
    types = models.ForeignKey('main.Types', related_name='products', on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type_of_price = models.CharField(max_length=20, choices=PriceTypeChoices, default='none-type-of-price')
    description = models.TextField()
    pictures = models.ImageField(upload_to='static/listing_images/')
    name = models.CharField(max_length=150)
    telephone_number = models.CharField(max_length=100)
