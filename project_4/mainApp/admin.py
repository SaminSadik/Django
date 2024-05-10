from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.mainModel)
admin.site.register(models.extraModel)