import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from webservice.helper import UUIDEncoder
from webservice.models import Faq, Company, CompanyProduct
from webservice.models import Product, ProductRelation, VehicleManufacture, VehicleModel, VehicleType


@csrf_exempt
@require_http_methods(["GET"])
def list_product_make(request, category):
    product_object = ProductRelation.objects.filter(car_manufacture__vehicle_category__pk=category).order_by(
        'car_manufacture').distinct('car_manufacture')

    p = [row.car_manufacture.to_json() for row in product_object]

    payload = {"status": True,
               "description": "Product Manufacture",
               "manufacture": p}
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


@csrf_exempt
@require_http_methods(["GET"])
def list_product_model(request, category, manufacture):
    product_object = ProductRelation.objects.filter(car_manufacture__unique_id=manufacture).order_by(
        'car_model').distinct('car_model')

    p = [row.car_model.to_json() for row in product_object]

    payload = {"status": True,
               "description": "Product Model",
               "model": p}
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


@csrf_exempt
@require_http_methods(["GET"])
def list_product_type(request, model):
    product_object = ProductRelation.objects.filter(car_model__unique_id=model).order_by('car_type').distinct(
        'car_type')

    p = [row.car_type.to_json() for row in product_object]

    payload = {"status": True,
               "description": "Product Type",
               "type": p}
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


@csrf_exempt
@require_http_methods(["GET"])
def list_product_type(request, type):
    product_object = Product.objects.filter(car_type__unique_id=type).order_by('car_type').distinct('car_type')

    p = [row.car_type.to_json() for row in product_object]

    payload = {"status": True,
               "description": "Product Type",
               "type": p}
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


@csrf_exempt
@require_http_methods(["GET"])
def list_product_filter(request, type):
    product_object = ProductRelation.objects.filter(car_type__unique_id=type)

    p = [row.product.to_json() for row in product_object]

    payload = {"status": True,
               "description": "Product Filtered",
               "product": p}
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


@csrf_exempt
@require_http_methods(["GET"])
def product_filter(request):
    category = request.GET.get('category', None)
    manufacture = request.GET.get('manufacture', None)
    model = request.GET.get('model', None)
    type = request.GET.get('type', None)

    if category is not None and manufacture is not None and model is not None and type is not None:
        product_filter = ProductRelation.objects.filter(car_category__pk=category,
                                                        car_manufacture__unique_id=manufacture,
                                                        car_model__unique_id=model,
                                                        car_type__unique_id=type).order_by('product').distinct().exclude(product__name="NO EXISTE").values('product')
        p = [get_product_by_id(row["product"]) for row in product_filter]
        payload = {"status": True,
                   "description": "Product Filtered By Category, Manufacture, Model, Type",
                   "product": p}

    elif category is not None and manufacture is not None and model is not None:
        product_filter = ProductRelation.objects.filter(car_category__pk=category,
                                                        car_manufacture__unique_id=manufacture,
                                                        car_model__unique_id=model).order_by('car_type').distinct().exclude(product__name="NO EXISTE").values('car_type')
        p = [get_type(row["car_type"]) for row in product_filter]
        payload = {"status": True,
                   "description": "Product Filtered By Category, Manufacture, Model",
                   "type": p}

    elif category and manufacture:
        product_filter = ProductRelation.objects.filter(car_category__pk=category,
                                                        car_manufacture__unique_id=manufacture).order_by('car_model').distinct().exclude(product__name="NO EXISTE").values('car_model')
        p = [get_model(row["car_model"]) for row in product_filter]
        payload = {"status": True,
                   "description": "Product Filtered By Category, Manufacture",
                   "model": p}

    elif category:
        product_filter = ProductRelation.objects.filter(car_category__pk=category).order_by('car_manufacture').distinct().values('car_manufacture')
        p = [get_manufacture(row["car_manufacture"]) for row in product_filter]
        payload = {"status": True,
                   "description": "Product Filtered by Category",
                   "manufacture": p}

    else:
        p = []

        payload = {"status": True,
                   "description": "Product Filtered",
                   "product": p}

    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)
def get_manufacture(pk):
    try:
        return VehicleManufacture.objects.get(pk=pk).to_json()
    except VehicleManufacture.DoesNotExist:
        return None

def get_model(pk):
    try:
        return VehicleModel.objects.get(pk=pk).to_json()
    except VehicleModel.DoesNotExist:
        return None

def get_type(pk):
    try:
        return VehicleType.objects.get(pk=pk).to_json()
    except VehicleType.DoesNotExist:
        return None

@csrf_exempt
@require_http_methods(["GET"])
def list_companies(request):
    list_companies = Company.objects.all()
    json_dict = [row.to_json() for row in list_companies]

    payload = {
        "status": True,
        "company": json_dict
    }
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


@csrf_exempt
@require_http_methods(["GET"])
def list_company_products(request, id):
    list_companies = CompanyProduct.objects.filter(company__id=id)
    json_dict = [row.to_json() for row in list_companies]

    payload = {
        "status": True,
        "company_product": json_dict
    }
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


# View list of products with no filtering or
# ordering related to data
@csrf_exempt
@require_http_methods(["GET"])
def list_product(request):
    limit = request.GET.get('limit', 1)
    random = request.GET.get('random', None)
    unique = request.GET.get('unique', None)
    engine = request.GET.get('engine', None)

    # if random == "0":
    #     order = '-name'
    # else:
    #     order = '?'

    if unique is not None:
        product_object = Product.objects.all().order_by('name').values('name').exclude(name="NO EXISTE").distinct()

    elif engine is not None:
        product_object = Product.objects.filter(engine=engine).order_by('name').values('name').exclude(
            name="NO EXISTE").distinct()
    elif limit != "1":
        # OrderNotes.objects.filter(item=item).values_list('shared_note', flat=True).distinct()
        product_object = Product.objects.all().order_by('name').values('name').exclude(name="NO EXISTE").distinct()[:int(limit)]
    else:
        product_object = Product.objects.all().order_by('name').values('name').exclude(name="NO EXISTE").distinct()

    p = [get_product(name=row["name"]) for row in product_object]

    payload = {"status": True, "product": p}
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)

def get_product(name):
    obj = Product.objects.filter(name=name).first()
    if obj:
        return obj.to_json()
    else:
        return None

def get_product_by_category(category):
    try:
        return Product.objects.get(category=category).to_json()
    except Product.DoesNotExist:
        return None

def get_product_by_id(pk):
    try:
        return Product.objects.get(pk=pk).to_json()
    except Product.DoesNotExist:
        return None

@csrf_exempt
@require_http_methods(["GET"])
def search_product(request, manufacture, model, type):
    product_object = ProductRelation.objects.filter(car_manufacture=manufacture,
                                                    car_model=model,
                                                    car_type=type
                                                    ).exclude(product__name='NO EXISTE')

    p = [row.to_json() for row in product_object]

    payload = {"status": True, "product": p}
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


@csrf_exempt
@require_http_methods(["GET"])
def list_unique_products(request):
    product_object = Product.objects.all()

    # .order_by('photo__name', 'photo__url').distinct('photo__name', 'photo__url')

    p = [row.to_json() for row in product_object]

    payload = {"status": True, "product": p}
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


# View product information, and details regarding
# relationship between master table
@csrf_exempt
@require_http_methods(["GET"])
def view_product(request, uk):
    try:
        product_object = Product.objects.get(unique_key=uk)
        payload = {"status": True, "product": product_object.to_json()}
        return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                            content_type='application/json',
                            status=200)
    except Product.DoesNotExist:
        payload = {"status": False}
        return HttpResponse(json.dumps(payload, indent=2),
                            content_type='application/json',
                            status=404)


@csrf_exempt
@require_http_methods(["GET"])
def get_faq(request):
    list_obj = Faq.objects.all()
    p = [row.to_json() for row in list_obj]
    payload = {"status": True, "faq": p}
    return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                        content_type='application/json',
                        status=200)


@csrf_exempt
@require_http_methods(["GET"])
def view_faq(request, uk):
    try:
        faq_obj = Faq.object.get(unique_key=uk)
        payload = {"status": True, "faq": faq_obj.to_json()}
        return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                            content_type='application/json',
                            status=200)

    except Faq.DoesNotExist:
        payload = {"status": False}
        return HttpResponse(json.dumps(payload, indent=2, cls=UUIDEncoder),
                            content_type='application/json',
                            status=404)
