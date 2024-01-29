import json
import datetime
from uuid import UUID
from decimal import Decimal

from django.contrib.humanize.templatetags.humanize import naturalday


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        # Encode UUID
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return str(obj)
        # Encode Dates
        if isinstance(obj, datetime.datetime):
            return str(naturalday(obj))

        if isinstance(obj, datetime.date):
            return str(naturalday(obj))

        if isinstance(obj, Decimal):
            return float(round(obj, 1))
        return json.JSONEncoder.default(self, obj)