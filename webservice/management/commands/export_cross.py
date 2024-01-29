import json
import time
import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from webservice.models import *



class Command(BaseCommand):

    def handle(self, *args, **options):

        not_in = []
        dat = Datasheet.objects.all()
        for row in dat:
            try:
                dat = ProductRelation.objects.filter(car_type=row.vehicle_type).first()
            except ProductRelation.DoesNotExist:
                not_in.append(row)

        print(len(not_in))
        # print(not_in)