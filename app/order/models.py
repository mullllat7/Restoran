from django.contrib.auth import get_user_model
from django.db import models

from app.resto.models import Resto

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    resto = models.ForeignKey(Resto, on_delete=models.CASCADE, related_name='comment')
    order_time = models.TimeField()
    date = models.DateField(null=True)
    amount_of_people = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.resto.resto_name}'

