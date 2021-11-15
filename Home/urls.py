
from enum import auto
from os import name
from django.urls import path, include
from .views import index, search_sku, autocomplite

urlpatterns = [

    path('', index, name="index"),
    path('search/', search_sku, name="search_list"),
    path('auto', autocomplite, name="autocomplite")
]
