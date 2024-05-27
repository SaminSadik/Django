from django.db import models

# Create your models here.
class BrandModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    def __str__(self):
        return self.name