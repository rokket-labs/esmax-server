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

        with open('/app/csv_products_dump.csv') as csvfile:
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

                p = Product(
                            name=row[0],
                            description=row[11],
                            engine=engine,
                            mobil=row[4],
                            shell_helix=row[5],
                            total=row[6],
                            ypf=row[7],
                            texaco=row[8],
                            castrol=row[9],
                            valvoline=row[10],
                            pdf=row[15])
                p.save()

                # if "Contenedor" in row[13]:
                #     p.uses.add(contenedor)
                #
                # if "Balde" in row[13]:
                #     p.uses.add(balde)
                #
                # if "Cuñete" in row[13]:
                #     p.uses.add(cunete)
                #
                # if "Tambor" in row[13]:
                #     p.uses.add(tambor)
                #
                # if "1-4 lt" in row[13]:
                #     p.uses.add(litro14)
                #
                # if "1-3 lt" in row[13]:
                #     p.uses.add(litro13)
                #
                # if "200-500 cc" in row[13]:
                #     p.uses.add(cclitro)
                #
                # if "500 cc" in row[13]:
                #     p.uses.add(cclitro)
                #
                # if "0,5-2,5 kg" in row[13]:
                #     p.uses.add(litrokg)
                #
                # if "Cuñete (54,5 kg)" in row[13]:
                #     p.uses.add(cunete54)




                # USES
                # if "Automovil" in row[12]:
                #     p.formats.add(auto)
                #
                # if "Moto" in row[12]:
                #     p.formats.add(moto)
                #
                # if "Transporte" in row[12]:
                #     p.formats.add(camion)
                #
                # if "Agricola" in row[12]:
                #     p.formats.add(tractor)
                #
                # if "Maq" in row[12]:
                #     p.formats.add(tractor)



                # p.uses.add(auto, camion, tractor, moto)
                # p.formats.add(tambor, balde, litro, contenedor)

                # print(row[0])
                # print(row[0], row[1], row[2], )
