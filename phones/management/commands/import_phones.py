import csv
from datetime import datetime
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    parser.add_argument('phones.csv', type=str)

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                id = int(line[0])
                name = line[1]
                price = line[3]
                image = line[2]
                release_date = datetime.strptime(line[4], '%Y-%m-%d').date()
                lte_exists = bool(line[5])
                slug = slugify(name)

                phone = Phone(
                    id=id,
                    name=name,
                    price=price,
                    image=image,
                    release_date=release_date,
                    lte_exists=lte_exists,
                    slug=slug,
                )
                phone.save()
