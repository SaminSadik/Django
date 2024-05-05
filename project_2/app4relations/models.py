from django.db import models
from app4models.models import myModel, myTable # for accessing models from another app

class exampleModel(models.Model): # used for demostrating 1toMANY rel later down
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, null=True, blank=True) # used for custom URLS
    def __str__(self): return self.name
    # even without str method, admin panel appearance can be changed in admin.py class

class relationModel(models.Model):
    #? 1to1 syntax: models.OneToOneField(to=related_model , on_delete=models.__ , othersOptional...)
    account = models.OneToOneField(to=myModel, on_delete=models.CASCADE)
    # deleting account doesn't automatically delete the related myModel instance
    # but if myModel instanmce is deleted, the corresponding relationModel instance will be deleted (for CASACADE)
    # for OneToOne relation, only 1 myModel instance can be related to 1 relationModel instance 

    #? 1toMANY syntax: models.ForeignKey(to=related_model, on_delete=models.__ , othersOptional...)
    speciality = models.ForeignKey(exampleModel, on_delete=models.CASCADE)
    #* Here, ONE exampleModel can have MANY relationModel, not the other way around *#
    # if an exampleModel instance is deleted, the related relationModel instances will be deleted (for CASACADE)
    # writing 'to=' is optional, but having to & on-delete is required

    #? MANYtoMANY syntax: models.ManyToManyField(related_model, related_name='name', othersOptional...)
    category = models.ManyToManyField(myTable, related_name='category')
    # on_delete isn't required for MANY to MANY relations
    # if an intsance in myTable gets deleted, the whole category won't be deleted
    # relations can be made with both the same app models AND other apps models OR either

    def __str__(self):
        return f"{self.account.full_name} - {self.speciality.name}"