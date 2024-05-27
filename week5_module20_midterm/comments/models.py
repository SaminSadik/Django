from django.db import models
from cars.models import CarModel

# Create your models here.
class CommentModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    def __str__(self):
        return f"Comment {self.id} - {self.car.name}"