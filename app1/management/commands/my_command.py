from django.core.management.base import BaseCommand
from app1.models import Сlient, Product
class Command(BaseCommand):
    help = "Print 'Hello world!' to output."
    def handle(self, *args, **kwargs):
        self.stdout.write('Hello world!')
