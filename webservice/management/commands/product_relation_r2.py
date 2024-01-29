import csv
from django.core.management.base import BaseCommand
from webservice.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        # /var/www/html/esmaxws/2019productos.csv
        with open('/var/www/html/esmaxws/csv_data/2019productos.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            # readCSV.next()
            found = 0
            notfound = 0
            dict_notfound = []

            # ++ DICT: ['TOTAL', 'Rubia S 10W', 'Dynatrans MPV', 'Transmission Axle 7 85W-140', 'Carter SH 150',
            #           'Carter SH 220', 'Carter SH 320']

            for row in readCSV:

                print("+++++++++++++++++++++++++++++++++++++++++++++++++")
                total = row[0]
                lubrax = row[1]

                print(" procesando.. total: {} -- lubrax: {}".format(total, lubrax))

                try:
                    print('se consiguio producto lubrax')

                    product_object = Product.objects.get(name__exact="Lubrax Turbo SAE 10W")
                    datasheet_obj = Datasheet.objects.filter(value__icontains="Rubia S 10W")

                    for row in datasheet_obj:
                        found += 1
                        print('se consiguio equivalencia en datasheet')
                        print("category: {}".format(row.vehicle_category))
                        print("manufacture: {}".format(row.vehicle_manufacture))
                        print("model: {}".format(row.vehicle_model))
                        print("type: {}".format(row.vehicle_type))

                        product_relation_object = ProductRelation(
                            car_category=row.vehicle_category,
                            car_manufacture=row.vehicle_manufacture,
                            car_model=row.vehicle_model,
                            car_type=row.vehicle_type,
                            product=product_object
                        )
                        product_relation_object.save()
                        print(' se salvo equivalencia')

                except Product.DoesNotExist:
                    notfound += 1
                    dict_notfound.append(total)
                    print("{} no existe".format(lubrax))

            print("+++++++++++++++++++++++++++++++++++++++++++++++++")
            print("++ FOUND: {}  NOT FOUND: {}".format(found, notfound))
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")
            print("++ DICT: {}".format(dict_notfound))
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")
