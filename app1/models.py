from django.db import models
from django.utils import timezone
# Create your models here.
class SaveCoin(models.Model):
    coin = (("О","Орел"),("Р","Решка"))
    coin_var = models.CharField(max_length=1,choices=coin)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"-{self.coin_var}-  "

    class Meta:
        ordering = ["-date"]
    @staticmethod
    def get_n(n):
        print(SaveCoin.objects.all()[:n])
        return SaveCoin.objects.all()[:n]

class Сlient(models.Model):
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=80)
    telNumber = models.CharField(max_length=11)
    adress = models.CharField(max_length=25)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f'Покупатель:{self.name} почта:{self.mail} телефон:{self.telNumber} адрес:{self.adress}'
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=180)
    price = models.FloatField()
    quantity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='product_image/')
    def __str__(self) -> str:
        return f'Продукт:{self.name} Описание:{self.title} Цена:{self.price} Колличестрво:{self.quantity}'
    
class Order(models.Model):
    client = models.ForeignKey(Сlient, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_order = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f'Клиент:{self.client} Продукты:{self.product} Сумма заказа:{self.total_order}'