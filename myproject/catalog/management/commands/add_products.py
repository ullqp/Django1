from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Clear db and load fixtures'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        fixtures = [
            'categories_fixture.json',
            'products_fixture.json'
        ]

        fixtures = ["catalog/management/fixtures/"+i for i in fixtures]

        for f in fixtures:
            call_command('loaddata', f)
