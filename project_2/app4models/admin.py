# run the command in terminal: py manage.py createsuperuser
# add /admin to home url & login with superuser credentials

from django.contrib import admin
from . import models # to use the classes in models.py here

# Register your models here.
admin.site.register(models.myTable)
admin.site.register(models.myModel)
# each model needs to be registered here to be used in the admin panel