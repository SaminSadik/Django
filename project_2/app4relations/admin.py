from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.relationModel)

# admin.site.register(models.exampleModel)
class exampleModel_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # to prepopulate slug using other fields
    list_display = ['name',] # all displayable fields will still remain visible
# list_display overrides __str__ method completely as admin panel display name
admin.site.register(models.exampleModel, exampleModel_Admin) # passing a class while registering