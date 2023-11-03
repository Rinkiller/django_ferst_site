from django.core.management.base import BaseCommand
from app1.models import Сlient

class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        for i in range(1,10):
            client = Сlient(name='John'+str(i), mail='john'+str(i)+'@example.com',telNumber='secret'+str(i), adress=25)
            client.save()
            self.stdout.write(f'{client}')