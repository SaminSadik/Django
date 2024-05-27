from django.db import models
from cars.models import CarModel
from django.contrib.auth.models import User

# Create your models here.
class OrderModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING, related_name='selected_car')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_set')
    time = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()
    contact_number = models.CharField(max_length=15)
    def __str__(self):
        return f"Order {self.id} - {self.car.name}"