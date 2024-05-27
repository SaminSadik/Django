from django.db import models
from brands.models import BrandModel

# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    def __str__(self):
        return f"{self.brand.name} - {self.name}"