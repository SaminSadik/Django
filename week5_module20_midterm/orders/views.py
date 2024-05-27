from django.shortcuts import render, redirect
from django.contrib import messages
from cars.models import CarModel
from .models import OrderModel
from .forms import OrderForm

def Order(request, car_slug):
    if request.user.is_authenticated:
        User = request.user
        Car = CarModel.objects.get(slug=car_slug)

        if request.method == 'POST':
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                order_form.instance.car = Car
                order_form.instance.user = User
                order_form.save()
                Car.quantity -= 1
                Car.save()
                messages.success(request, "Your order is confirmed. Thanks for shopping.")
                return redirect('profile')
        else:
            order_form = OrderForm()
        return render(request, 'order.html', {'form': order_form, 'User': User, 'Car': Car})
    
    else:
        messages.warning(request, "Must be logged in to buy anything!")
        return redirect('login')