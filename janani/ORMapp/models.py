from django.db import models
from django.contrib import admin
class owner(models.Model):
    car_no=models.IntegerField()
    colour=models.CharField(max_length=10)
    product_no=models.IntegerField()
    brand=models.CharField(max_length=10)
    waranty=models.IntegerField()
class ownerAdmin(admin.ModelAdmin):
    list_display=["car_no","colour","product_no","brand","waranty"]   

