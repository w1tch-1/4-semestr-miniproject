from django.db import models
from django_lifecycle import LifecycleModel, hook, BEFORE_SAVE
from django.core.exceptions import ValidationError


class Response(LifecycleModel, models.Model):
    AMOUNT_PER_USER_PER_PRODUCT = 10

    user = models.ForeignKey('user.User', related_name='responses', on_delete=models.SET_NULL, null=True)
    listing = models.ForeignKey('main.Listing', related_name='responses', on_delete=models.CASCADE)

    text = models.TextField()

    @hook(BEFORE_SAVE)
    def check_responses_amount_constraint(self):
        if Response.objects.filter(user=self.user, listing=self.listing).count() >= 10:
            raise ValidationError('Amount must be less than 10')
