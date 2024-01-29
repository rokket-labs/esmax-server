import requests
from django.core.management.base import BaseCommand
from pyquery import PyQuery as pq

from webservice.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):

        r = requests.get(url="https://www.esmax.cl/listado-lubricantes/")

        if r.status_code == 200:
            document_html = pq(r.content)
            if document_html:
                rows = document_html("#tab_lubricantes > div > article")
                for row in rows:
                    product_array = pq(row).find('div > div > div > div')
                    for item in product_array:

                        title = pq(item).find('.wpsm_panel-heading').text()
                        if title is None:
                            print("titulo vacio")
                        else:
                            image_url = pq(item).find('.size-thumbnail').attr("src")
                            if image_url is not None and len(title) != 0:

                                product_name = str(title.replace("LUBRAX",""))

                                print(product_name)
                                print(image_url)

                                p_obj = Product.objects.filter(name__icontains=product_name)

                                for p in p_obj:
                                    p.image = image_url
                                    p.save()

            else:
                print("Documento vacio")
        else:
            print("Fallo request")

