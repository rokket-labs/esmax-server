from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import Group

from webservice.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'engine', 'description')
    search_fields = ["name"]
    list_filter = ["engine", "uses", "formats"]


class DatasheetAdmin(admin.ModelAdmin):

    list_display = ('vehicle_manufacture', 'vehicle_model', 'vehicle_type','vehicle_category')
    search_fields = ["value"]
    list_filter = ["vehicle_category"]

#
class ProductRelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_manufacture', 'car_model', 'car_type', 'product')
    search_fields = ["product"]
    list_filter = ["car_manufacture", "product" ]


class FormatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ["name"]


class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    # list_editable = ["category"]


class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_type')
    # list_editable = ["category"]
    search_fields = ["vehicle_type"]


class VehicleManufactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')
    list_editable = ["brand"]


class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_model')


class UseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ["name"]


class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CompanyProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'company')

admin.site.register(ProductRelation, ProductRelationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Formats, FormatAdmin)
admin.site.register(Company, CompanyAdmin)

admin.site.register(CompanyProduct, CompanyProductAdmin)

admin.site.register(Uses, UseAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(VehicleCategory, VehicleCategoryAdmin)
admin.site.register(VehicleManufacture, VehicleManufactureAdmin)
admin.site.register(VehicleModel, VehicleModelAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(Datasheet,DatasheetAdmin)
admin.site.unregister(Group)
