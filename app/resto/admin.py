from django.contrib import admin

from app.resto.models import Resto, Food, Menu, RestoImage, FoodImage, MenuImage


class RestoImageAdmin(admin.TabularInline):
    model = RestoImage
    fields = ()
    extra = 1


@admin.register(Resto)
class RestoAdmin(admin.ModelAdmin):
    list_display = ('resto_name', 'adress')
    list_display_links = ('resto_name', 'adress')
    search_fields = ['resto_name', 'adress']
    list_filter = ('resto_name', 'adress')
    inlines = [RestoImageAdmin]


class MenuImageAdmin(admin.TabularInline):
    model = MenuImage
    fields = ()
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu',)
    list_display_links = ('menu',)
    search_fields = ['menu']
    list_filter = ('menu',)
    inlines = [MenuImageAdmin]


class FoodImageAdmin(admin.TabularInline):
    model = FoodImage
    fields = ()
    extra = 1


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name_of_food', 'price', 'weight', 'ingredients')
    list_display_links = ('name_of_food', 'price', 'weight', 'ingredients')
    search_fields = ['name_of_food', 'price', 'weight', 'ingredients']
    list_filter = ('name_of_food', 'price', 'weight', 'ingredients')
    inlines = [FoodImageAdmin]

