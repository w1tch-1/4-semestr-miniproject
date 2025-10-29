from django.db import models
from django_lifecycle import LifecycleModel, hook, AFTER_SAVE
from django.core.mail import send_mail


class Order(LifecycleModel, models.Model):
    user = models.ForeignKey('user.User', related_name='orders',  on_delete=models.CASCADE, null=True)
    listing = models.ManyToManyField('main.Listing', related_name='orders')
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @hook(AFTER_SAVE)
    def send_email(self):
        message = f"Thank you for your order!\n\nItems:{self.title}\n\nTotal: {self.price}€"

        send_mail(
            'New Order',
            message,
            'kubertv44@gmail.com',
            [self.user.email],
            fail_silently=False,
        )
