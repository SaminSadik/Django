from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assigned_date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title