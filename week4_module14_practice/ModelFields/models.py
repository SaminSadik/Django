from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=20, default='')  
    address = models.TextField(default='')
    email = models.EmailField(default='example@gmail.com')
    date = models.DateField(default=datetime.today)  
    time = models.TimeField(default=timezone.now)
    duration = models.DurationField(default=timedelta())   
    null_boolean_field = models.BooleanField(default=None, null=True, blank=True)  
    url_field = models.URLField(default='http://phitron.io/')
    
    def __str__(self) -> str:
        return f"{self.roll} - {self.name}"