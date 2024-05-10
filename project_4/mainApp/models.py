from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class mainModel(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # pic = models.ImageField(upload_to='media/', blank=True) # goes in project
    pic = models.ImageField(upload_to='mainApp/media/', blank=True) # goes in app
    def __str__(self):
        return f"{self.owner} - {self.name}"
    
class extraModel(models.Model):
    connection = models.ForeignKey(mainModel, on_delete=models.CASCADE, related_name='comments')
    # related_name makes a reverse relationship to access extraModel through mainModel
    credit = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return f"Comment #{self.id}"