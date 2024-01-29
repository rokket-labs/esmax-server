from django.core.management.base import BaseCommand

from webservice.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            print('se consiguio producto lubrax')

            product_object = Product.objects.get(id=44378)
            datasheet_obj = Datasheet.objects.filter(value__icontains="Carter SH 320")

            for row in datasheet_obj:
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
            print("Does not exists")
