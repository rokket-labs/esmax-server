# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [

    path('product/make/<int:category>', views.list_product_make),
    path('product/model/<uuid:manufacture>', views.list_product_model),
    path('product/type/<uuid:model>', views.list_product_type),
    path('product/filter/<uuid:type>', views.list_product_filter),
    path('product/filter/', views.product_filter),
    path('company/',views.list_companies),
    path('company/<int:id>', views.list_company_products),
    path('product/', views.list_product),
    path('product/<uuid:uk>', views.view_product),
    path('product/search/<int:manufacture>/<int:model>/<int:type>', views.search_product),
    path('faq/', views.get_faq),
    path('faq/<uuid:uk>', views.view_faq),

]
