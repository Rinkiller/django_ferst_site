from django import forms
from .models import Product, Сlient

class ProductForm(forms.Form):
    name = forms.CharField(max_length=30)
    title = forms.CharField(max_length=180)
    price = forms.FloatField()
    quantity = forms.IntegerField()
    image = forms.ImageField()

class СlientForm(forms.Form):
    name = forms.CharField(max_length=20)
    mail = forms.EmailField()
    telNumber = forms.CharField(max_length=11)
    adress = forms.CharField(max_length=25)

class OrderForm(forms.Form):
    name = forms.CharField(max_length = 20, label = 'Имя клиента')
    product_id = forms.ChoiceField(label = 'Название продукта', choices  = [(prod.id,prod.name) for prod in Product.objects.all()])
    total_order = forms.IntegerField(label = 'Количество шт.')

class Client_id(forms.Form):
    client_id = forms.ChoiceField(label = 'Имя клиента', choices  = [(cli.id,cli.name) for cli in Сlient.objects.all()])