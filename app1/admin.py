from django.contrib import admin
from .models import SaveCoin, Сlient, Product, Order
# Register your models here.
@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

@admin.register(Сlient)
class СlientAdmin(admin.ModelAdmin):
    list_display = ['name','mail','telNumber','adress']
    list_filter = ['date']

#Настройте под свои нужды вывод информации о клиентах, товарах и заказах на страницах 
# вывода информации об объекте и вывода списка объектов.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name','-price']
    search_fields = ['name']
    list_filter = ['date']
    search_fields = ['title']
    search_help_text = 'Поиск по полю Описание продукта(title)'
    actions = [reset_quantity]
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'total_order']
    ordering = ['client','-total_order']
    list_filter = ['date']