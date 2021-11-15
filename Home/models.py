from django.db import models

# Create your models here.


class Sku(models.Model):

    sku_id = models.IntegerField(max_length=150, blank=True, null=True)
    product_id = models.IntegerField(max_length=150, blank=True, null=True)
    sku_name = models.CharField(max_length=450, blank=True, null=True)
    price = models.CharField(max_length=450, blank=True, null=True)
    manufacturer_name = models.CharField(max_length=450, blank=True, null=True)
    salt_name = models.CharField(max_length=450, blank=True, null=True)
    drug_form = models.CharField(max_length=450, blank=True, null=True)
    Pack_size = models.CharField(max_length=450, blank=True, null=True)
    strength = models.CharField(max_length=450, blank=True, null=True)
    product_banned_flag = models.CharField(
        max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=450, blank=True, null=True)
    price_per_unit = models.CharField(max_length=450, blank=True, null=True)
