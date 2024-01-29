import json
import time
import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from webservice.models import *
import pandas as pd
import numpy as np


class Command(BaseCommand):

    def handle(self, *args, **options):
        # df = pd.read_csv('/app/products.csv',
        #                  names=['product_name', 'Clasificacion1', 'Clasificacion2', 'DescripcionAPP', 'Total',
        #                         'Description', 'Use', 'formats', 'image', 'Pdf'])
        #
        # print(df["Total"])

        product_search = "Rubia K 50"
        name = "LUBRAX TURBO 50"
        desc = "Aceite monogrado para motores diesel de aspiración natural en diversas condiciones de servicio. Aplica en transmisiones PowerShift, también en flotas mixtas. Cumple API CF y API SF."
        pdf = "http://www.esmax.cl/wp-content/uploads/2018/03/TDS-Lubrax-Turbo.pdf"

        datasheet_obj = Datasheet.objects.filter(value__icontains=product_search)
        print(datasheet_obj.count())

        for row in datasheet_obj:
            # USES
            camion = Uses.objects.get(id=4)
            tractor = Uses.objects.get(id=3)
            auto = Uses.objects.get(id=2)
            moto = Uses.objects.get(id=1)

            # FORMATS
            contenedor = Formats.objects.get(id=4)
            balde = Formats.objects.get(id=3)
            tambor = Formats.objects.get(id=2)
            litro = Formats.objects.get(id=1)

            # TYPE_CHOICES = (
            #     (1, 'Gasolina'),
            #     (2, 'Diesel'),
            #     (3, 'Gas'),
            #     (4, 'Electrico'),
            # )

            p = Product(car_manufacture=row.vehicle_manufacture,
                        car_model=row.vehicle_model,
                        car_type=row.vehicle_type,
                        name=name,
                        description=desc,
                        engine=2,
                        pdf=pdf)
            p.save()
            p.uses.add(auto, camion, tractor, moto)
            p.formats.add(tambor, balde, litro, contenedor)

            print("created product...")
