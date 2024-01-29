from django.core.management.base import BaseCommand, CommandError
from webservice.models import *
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):

        # product_object = Product.objects.all()
        #
        # with open('/app/csv_export.csv', 'w') as csvFile:
        #     writer = csv.writer(csvFile)
        #
        #     writer.writerow(['id', 'manufacture', 'model', 'type', 'product'])
        #
        #     field_list = [[str(f.id),
        #                    str(f.car_manufacture),
        #                    str(f.car_model),
        #                    str(f.car_type),
        #                    str(f.name)]
        #                   for f in product_object]
        #
        #     writer.writerows(field_list)

        with open('/var/www/html/esmaxws/csv_products_dump.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            # readCSV.next()

            for row in readCSV:

                print(row[0])

                # USES
                use1 = Uses.objects.get(name="Automovil")
                use2 = Uses.objects.get(name="Moto")
                use3 = Uses.objects.get(name="Transporte")
                use4 = Uses.objects.get(name="Maquinaria Agricola")
                use5 = Uses.objects.get(name="Maquinaria Vial")
                use6 = Uses.objects.get(name="Lancha")
                use7 = Uses.objects.get(name="Moto Agua")
                use8 = Uses.objects.get(name="Industria")

                # FORMATS
                format1 = Formats.objects.get(name="1-4 Litro")
                format2 = Formats.objects.get(name="Cuñete")
                format3 = Formats.objects.get(name="Barril")
                format4 = Formats.objects.get(name="1-3 Litro")
                format5 = Formats.objects.get(name="Tambor")
                format6 = Formats.objects.get(name="Balde")
                format7 = Formats.objects.get(name="Cuñete (54,5 Kg)")
                format8 = Formats.objects.get(name="0,5-2,5 Kg")
                format9 = Formats.objects.get(name="200-500 cc")
                format10 = Formats.objects.get(name="Contenedor")



                # TYPE_CHOICES = (
                #     (1, 'Gasolina'),
                #     (2, 'Diesel'),
                #     (3, 'Gas'),
                #     (4, 'Electrico'),
                # )


                if "Aceite de Motores Gasolineros" in row[3]:
                    engine = 1
                elif "Aceite de Motores Diesel" in row[3]:
                    engine = 2
                elif "Aceite Transmisión" in row[3]:
                    engine = 3
                elif "Aceites Hidraulicos" in row[3]:
                    engine = 4
                elif "Aceites de Motor a Gas" in row[3]:
                    engine = 5
                elif "Refrigerantes" in row[3]:
                    engine = 6
                elif "Especialidades Automotrices" in row[3]:
                    engine = 7
                elif "Aceite Industriales" in row[3]:
                    engine = 9
                elif "Grasas" in row[3]:
                    engine = 8
                else:
                    engine = 1


                try:
                    po = Product.objects.get(name=row[0])
                    po.description = row[11]
                    po.engine = engine
                    po.mobil = row[4]
                    po.shell_helix = row[5]
                    po.total = row[6]
                    po.ypf = row[7]
                    po.texaco = row[8]
                    po.castrol = row[9]
                    po.valvoline = row[10]
                    po.pdf = row[15]
                    po.save()

                    formats = []
                    uses = []

                    if "Contenedor" in row[13]:
                        formats.append(format10)

                    if "Balde" in row[13]:
                        formats.append(format6)

                    if "Cuñete" in row[13]:
                        formats.append(format2)

                    if "Barril" in row[13]:
                        formats.append(format3)

                    if "Tambor" in row[13]:
                        formats.append(format5)

                    if "1-4 lt" in row[13]:
                        formats.append(format1)

                    if "1-3 lt" in row[13]:
                        formats.append(format4)

                    if "200-500 cc" in row[13]:
                        formats.append(format9)

                    if "0,5-2,5 kg" in row[13]:
                        formats.append(format8)

                    if "Cuñete (54,5 kg)" in row[13]:
                        formats.append(format7)

                    # USES
                    if "Automovil" in row[12]:
                        uses.append(use1)

                    if "Moto" in row[12]:
                        uses.append(use2)

                    if "Transporte" in row[12]:
                        uses.append(use3)

                    if "Agricola" in row[12]:
                        uses.append(use4)

                    if "Maq" in row[12]:
                        uses.append(use5)

                    if "Lancha" in row[12]:
                        uses.append(use6)

                    if "Moto Agua" in row[12]:
                        uses.append(use7)

                    if "Industria" in row[12]:
                        uses.append(use8)

                    po.uses.add(*uses)
                    po.formats.add(*formats)

                except Product.DoesNotExist:
                    print("product {} does not exist".format(row[0]))



                # print(row[0])
                # print(row[0], row[1], row[2], )
