import datetime
import os
import uuid

from django.conf import settings
from django.db import models

FORMAT_CHOICES = (
    (1, '1 Litro'),
    (2, '5 Litros'),
    (3, 'Bidon'),
    (4, '5 Galones'),
)

USE_CHOICES = (
    (1, 'Auto'),
    (2, 'Camion'),
    (3, 'Motos'),
    (4, 'Grua'),
    (5, 'Tractor'),
)

TYPE_CHOICES = (
    (1, 'Aceite de Motores Gasolineros '),
    (2, 'Aceite de Motores Diesel'),
    (3, 'Aceite Transmisión'),
    (4, 'Aceites Hidraulicos'),
    (5, 'Aceites de Motor a Gas'),
    (6, 'Refrigerantes'),
    (7, 'Especialidades Automotrices'),
    (8, 'Grasas'),
    (9, 'Aceite Industriales'),
)


def get_file_path(instance, filename):
    today = datetime.datetime.today()
    path = "img/{year}/{month}/".format(month=today.month,
                                        year=today.year)
    ext = filename.split('.')[-1]
    file_name = uuid.uuid4().hex
    filename = "{unique_name}.{extension}".format(unique_name=file_name,
                                                  extension=ext)

    return os.path.join(path, filename)


#
#
class Formats(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    def to_json(self):
        return {
            'name': self.name,
            'id': self.pk
        }


#
#
class Uses(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    def to_json(self):
        return {
            'name': self.name,
            'id': self.pk
        }


#
#
class VehicleCategory(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    category = models.CharField(max_length=250)
    update_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    vehicle_category_choice = (
        (1, 'Car'),
        (2, 'Van'),
        (3, 'Moto'),
        (4, 'Truck'),
        (5, 'Industrial Machine'),
        (6, 'Agricultural Machine')
    )

    def __str__(self):
        return '{}'.format(self.category)


#
#
class VehicleManufacture(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    vehicle_category = models.ForeignKey(VehicleCategory, on_delete=models.DO_NOTHING)
    remote_code = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    update_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.brand)

    def to_json(self):
        payload = {
            "id": str(self.unique_id),
            "brand": self.brand
        }
        return payload


#
#
class VehicleModel(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    vehicle_manufacture = models.ForeignKey(VehicleManufacture, on_delete=models.DO_NOTHING)
    vehicle_model = models.CharField(max_length=100)
    remote_code = models.CharField(max_length=50)
    update_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.vehicle_model)

    def to_json(self):
        payload = {
            "id": str(self.unique_id),
            "vehicle_model": self.vehicle_model
        }
        return payload


#
#
class VehicleType(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.DO_NOTHING)
    vehicle_type = models.CharField(max_length=100)
    remote_code = models.CharField(max_length=50)
    update_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.vehicle_type)

    def to_json(self):
        payload = {
            "id": str(self.unique_id),
            "type": self.vehicle_type
        }
        return payload


class Datasheet(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    origin_url = models.URLField()
    vehicle_category = models.ForeignKey(VehicleCategory, on_delete=models.DO_NOTHING)
    vehicle_manufacture = models.ForeignKey(VehicleManufacture, on_delete=models.DO_NOTHING)
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.DO_NOTHING)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.DO_NOTHING)
    title = models.TextField(null=True, blank=True)
    value = models.TextField(null=True, blank=True)

    update_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)


class Product(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    engine = models.IntegerField(choices=TYPE_CHOICES, default=1, blank=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    formats = models.ManyToManyField(Formats, related_name='formats')
    uses = models.ManyToManyField(Uses, related_name='uses')
    image = models.URLField(blank=True, null=True)
    pdf = models.URLField(blank=True, null=True)
    # Competitors
    mobil = models.CharField(max_length=100, blank=True, null=True)
    shell_helix = models.CharField(max_length=100, blank=True, null=True)
    total = models.CharField(max_length=100, blank=True, null=True)
    ypf = models.CharField(max_length=100, blank=True, null=True)
    texaco = models.CharField(max_length=100, blank=True, null=True)
    castrol = models.CharField(max_length=100, blank=True, null=True)
    valvoline = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    def to_json(self):

        domain = settings.DOMAIN

        # if self.image:
        #     image = "{}{}".format(domain, str(self.image))
        # else:
        #     image = "{}static/img/default.jpg".format(domain)

        if self.pdf:
            pdf = str(self.pdf)
        else:
            pdf = ""

        payload = {
            "unique_key": self.unique_key,
            "name": self.name,
            "engine": {
                "name": self.get_engine_display(),
                "id": self.engine
            },
            "description": self.description,
            "formats": [r.to_json() for r in self.formats.all()],
            "uses": [r.to_json() for r in self.uses.all()],
            "image": self.image,
            "pdf": pdf,
            "equivalent": [
                {
                    "name": "Mobil",
                    "product": self.mobil
                },
                {
                    "name": "Shell Helix",
                    "product": self.shell_helix
                },
                {
                    "name": "Total",
                    "product": self.total
                },
                {
                    "name": "YPF",
                    "product": self.ypf
                },
                {
                    "name": "Texaco",
                    "product": self.texaco
                },
                {
                    "name": "Castrol",
                    "product": self.castrol
                },
                {
                    "name": "Valvoline",
                    "product": self.valvoline
                }
            ]
        }
        return payload


class ProductRelation(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    car_category = models.ForeignKey(VehicleCategory, on_delete=models.DO_NOTHING, blank=True, null=True)
    car_manufacture = models.ForeignKey(VehicleManufacture, on_delete=models.DO_NOTHING, blank=True, null=True)
    car_model = models.ForeignKey(VehicleModel, on_delete=models.DO_NOTHING, blank=True, null=True)
    car_type = models.ForeignKey(VehicleType, on_delete=models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.product.name)

    def to_json(self):
        payload = {
            "product": self.product if self.product else []
        }
        return payload


class Company(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    def to_json(self):
        payload = {
            "id": self.id,
            "unique_key": str(self.unique_key),
            "company": self.name
        }
        return payload


class CompanyProduct(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)

    def to_json(self):
        payload = {
            "id": self.id,
            "unique_key": self.unique_key,
            "name": self.name,
            "product": self.product.to_json() if self.product else []
        }
        return payload


# Create your models here.
class Faq(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return '{}'.format(self.question)

    def to_json(self):
        payload = {
            "id": self.id,
            "question": self.question,
            "answer": self.answer
        }
        return payload
