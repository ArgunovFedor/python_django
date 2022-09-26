from django.core.management import BaseCommand

from app_shops.models import Shop


class Command(BaseCommand):
    help = 'Добавить 1000 магазинов'

    def handle(self, *args, **options):
        for i in range(100, 1100):
            Shop.objects.create(name=f'магазин {i}')

        self.stdout.write('Магазины успешно загружены')
