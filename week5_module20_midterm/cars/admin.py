from django.contrib import admin
from . import models

# Register your models here.
class Car_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} 
    list_display = ['name']

admin.site.register(models.CarModel, Car_Admin)