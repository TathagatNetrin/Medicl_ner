from os import replace
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import csv
from .models import Sku

# Create your views here.
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def autocomplite(request):
    if 'term' in request.GET:
        qs = Sku.objects.filter(
            sku_id__contains=request.GET.get('term')) | Sku.objects.filter(
            product_id__contains=request.GET.get('term')) | Sku.objects.filter(
            sku_name__istartswith=request.GET.get('term')) | Sku.objects.filter(
            price__contains=request.GET.get('term')) | Sku.objects.filter(
            manufacturer_name__istartswith=request.GET.get('term')) | Sku.objects.filter(
            salt_name__istartswith=request.GET.get('term')) | Sku.objects.filter(
            drug_form__istartswith=request.GET.get('term')) | Sku.objects.filter(
            Pack_size__contains=request.GET.get('term')) | Sku.objects.filter(
            strength__contains=request.GET.get('term')) | Sku.objects.filter(
            product_banned_flag__contains=request.GET.get('term')) | Sku.objects.filter(
            unit__contains=request.GET.get('term')) | Sku.objects.filter(
            price_per_unit__contains=request.GET.get('term'))
        title = list()
        for d in qs:

            title.append(d.sku_name)
            title.append(d.manufacturer_name)
            title.append(d.salt_name)
            title.append(d.drug_form)

        return JsonResponse(title[:15], safe=False)

    return render(request, 'index.html')


def search_sku(request):
    if request.method == 'POST':

        search_str = request.POST.get('search')
        sku = Sku.objects.filter(
            sku_id__contains=search_str) | Sku.objects.filter(
            product_id__contains=search_str) | Sku.objects.filter(
            sku_name__contains=search_str) | Sku.objects.filter(
            price__contains=search_str) | Sku.objects.filter(
            manufacturer_name__contains=search_str) | Sku.objects.filter(
            salt_name__contains=search_str) | Sku.objects.filter(
            drug_form__contains=search_str) | Sku.objects.filter(
            Pack_size__contains=search_str) | Sku.objects.filter(
            strength__contains=search_str) | Sku.objects.filter(
            product_banned_flag__contains=search_str) | Sku.objects.filter(
            unit__contains=search_str) | Sku.objects.filter(
            price_per_unit__contains=search_str)
        sku_list = Paginator(sku, 10)
        page = request.GET.get('page')
        try:
            sku = sku_list.page(page)
        except PageNotAnInteger:
            sku = sku_list.page(1)
        except EmptyPage:
            sku = sku_list.page(sku_list.num_pages)
        param = {'sku': sku}
        return render(request, 'index.html', param)


def index(request):

    with open('NER/meddata.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        cout = 0
        for line in csv_reader:
            sku_id = line[0].replace('.0', '')
            if sku_id == '-':
                sku_id = None
            else:
                sku_id = int(sku_id)
            product_id = line[1].replace('.0', '')
            if product_id == '-':
                product_id = None
            else:
                product_id = int(product_id)

            sku_name = line[2]
            price = line[3]
            manufacturer_name = line[4]
            salt_name = line[5]
            drug_form = line[6]
            Pack_size = line[7]
            strength = line[8]
            product_banned_flag = line[9]
            unit = line[10]
            price_per_unit = line[11]
            check = Sku.objects.filter(sku_name=sku_name).first()

            if check:
                pass
            else:

                metadata = Sku.objects.create(sku_id=sku_id, product_id=product_id,
                                              sku_name=sku_name, price=price, manufacturer_name=manufacturer_name,
                                              salt_name=salt_name, drug_form=drug_form, Pack_size=Pack_size, strength=strength,
                                              product_banned_flag=product_banned_flag, unit=unit, price_per_unit=price_per_unit)
                metadata.save()
                cout += 1
                print(sku_name, " sku data loading ....................100%")

            """each refrerece it will add 100 data 
            in db those data is not present in db"""

            if cout == 100:
                break

    sku_list = Paginator(Sku.objects.all(), 10)
    page = request.GET.get('page')
    try:
        sku = sku_list.page(page)
    except PageNotAnInteger:
        sku = sku_list.page(1)
    except EmptyPage:
        sku = sku_list.page(sku_list.num_pages)

    param = {'sku': sku}
    return render(request, 'index.html', param)
