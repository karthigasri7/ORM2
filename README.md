# Ex02 Django ORM Web Application
## Date: 6/10/25

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM

from django.contrib import admin
from .models import owner,ownerAdmin
admin.site.register(owner,ownerAdmin)

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




## OUTPUT
![alt text](<Screenshot 2025-10-06 231118.png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
