from django.db import models
from main.choices import PriceTypeChoices
from user.models import User
from star_ratings.models import Rating


class Listing(models.Model):
    category = models.ForeignKey('main.Category', related_name='products', on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey('main.SubCategory', related_name='products', on_delete=models.SET_NULL, null=True)
    types = models.ForeignKey('main.Types', related_name='products', on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type_of_price = models.CharField(max_length=20, choices=PriceTypeChoices.choices, default=PriceTypeChoices.FIXED_PRICE)
    description = models.TextField()
    pictures = models.ImageField(upload_to='listing_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    telephone_number = models.CharField(max_length=100)

    @property
    def rating(self):
        return Rating.objects.for_instance(self)
