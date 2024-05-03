from django.db import models # a model/class needs to inherit models.Model to work

# Create your models here.

class myTable(models.Model): # each class(model) represents a table in the database
    name = models.CharField(max_length=20) # length need to be specified in CharField
    ID = models.IntegerField(primary_key=True) # pk is unique, if not specified, django will make 'id' automatically

# after adding a model, run the following commands in the terminal:
# py manage.py makemigrations
# py manage.py migrate

# DB-browser app is used to modify the table/database (after migration)
# SQlite viewer extension is used to view the table in vscode

class myModel(models.Model):
    full_name = models.TextField(null=True) # will be NULL in table creation, but still required for subbmission
    email_address = models.EmailField(unique=True) # no date under this field can be the same
    cgpa = models.FloatField(verbose_name='CGPA') # if not specified Django takes the field name as Display name
    checkbox = models.BooleanField(default=False) # sets a default value even if nothing is entered
    profile = models.URLField(blank=True, null=True) # this field is no longer required to fill
    # id field is automatically created as no pk was specified here

    def __str__(self): # defines how the data is displayed in the admin panel
        return f"{self.id} - {self.full_name}"
        # without this, each entry in the table would be "modelname object (pk)"
    
    