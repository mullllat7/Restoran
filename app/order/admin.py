from django.contrib import admin

from app.order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'resto', 'order_time', 'amount_of_people', 'date')
    list_display_links = ('user', 'resto', 'order_time', 'amount_of_people' , 'date')
    search_fields = ['user', 'resto', 'order_time', 'amount_of_people', 'date']
    list_filter = ('user', 'resto', 'order_time', 'amount_of_people', 'date')


admin.site.register(Order, OrderAdmin)
