from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Resto(models.Model):

    resto_name = models.CharField(max_length=255, unique=True,  primary_key=True)
    opening_time = models.TimeField(default='06:00')
    closing_time = models.TimeField(default='00:00')
    adress = models.CharField(max_length=255)
    num_of_tables = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.resto_name


class RestoImage(models.Model):

    resto = models.ForeignKey(Resto, on_delete=models.CASCADE, related_name='resto_image')
    resto_image = models.ImageField(upload_to='')

    def __str__(self):
        return self.resto.resto_name


class Menu(models.Model):

    resto = models.ForeignKey(Resto, on_delete=models.SET_NULL, null=True, blank=True, related_name="food_type")
    menu = models.CharField(max_length=255, unique=True, primary_key=True)

    def __str__(self):
        return self.menu


class MenuImage(models.Model):

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_image')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.menu.menu


class Food(models.Model):

    name_of_food = models.CharField(max_length=255)
    resto = models.ForeignKey(Resto, on_delete=models.SET_NULL, null=True, blank=True, related_name='resto_name_menu')
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True, related_name='menu_menu')
    price = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    ingredients = models.CharField(max_length=1000,)

    def __str__(self):
        return self.name_of_food


class FoodImage(models.Model):

    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_image')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.food.name_of_food


class Saved(models.Model):
    user = models.ForeignKey(User, related_name='saved_resto', on_delete=models.CASCADE)
    resto = models.ForeignKey(Resto, related_name='saved', on_delete=models.CASCADE)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.saved}'
