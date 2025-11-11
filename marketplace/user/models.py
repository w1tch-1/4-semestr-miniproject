from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    seller_fullname = models.CharField(max_length=50, null=True)
    seller_company_name = models.CharField(max_length=60, null=True)
    seller_email = models.EmailField(null=True)
    is_seller = models.BooleanField(default=False, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='none')
