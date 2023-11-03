from django.core.management.base import BaseCommand
from app1.models import Product

class Command(BaseCommand):
    help = "Create product."
    def handle(self, *args, **kwargs):
        for i in range(1,10):
            product = Product(name='Product'+str(i), title='Product'+str(i)+' is very good', price=i*123.34, quantity=25+i)
            product.save()
            self.stdout.write(f'{product}')