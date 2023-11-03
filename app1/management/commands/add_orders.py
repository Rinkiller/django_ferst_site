from random import randint
from django.core.management.base import BaseCommand
from app1.models import Product, Сlient, Order

class Command(BaseCommand):
    help = "Create product."
    def handle(self, *args, **kwargs):
        for i in range(1,10):
            client = Сlient.objects.get(id=i)
            for j in range(1,randint(1,10)):
                product = Product.objects.get(id=j)
                ordr = Order(client=client,product=product, total_order = 10)
                ordr.save()
                self.stdout.write(f'{ordr}')

