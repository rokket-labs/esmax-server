from django.core.management.base import BaseCommand, CommandError
from webservice.models import *
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('/var/www/html/esmaxws/csv_data/dumpdata.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            # readCSV.next()

            for row in readCSV:
                print(row[0])

                try:
                    company = Company.objects.get(name=row[0])
                    try:
                        product = Product.objects.get(name__exact=row[2])

                        CompanyProduct(
                            company=company,
                            name=row[1],
                            product=product
                        ).save()
                    except Product.DoesNotExist:
                        print("product: {} does not exist".format(row[2]))
                except Company.DoesNotExist:
                    print("company: {} does not exist".format(row[0]))



