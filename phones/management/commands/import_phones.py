import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for ph in phones:
            dates = Phone(
                name = ph['name'],
                price = ph['price'],
                image = ph['image'],
                release_date = ph['release_date'],
                lte_exists = ph['lte_exists'],
                slug = slugify(ph['name'])
            )
            dates.save()
            print(dates)
        pass
