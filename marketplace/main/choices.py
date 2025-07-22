from django.db import models


class PriceTypeChoices(models.TextChoices):
    FIXED_PRICE = 'fp', 'Fixed price'
    VB = 'vb', 'VB'
    TO_GIVE_AWAY = 'tga', 'To give away'
