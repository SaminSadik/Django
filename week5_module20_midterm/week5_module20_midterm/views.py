from django.shortcuts import render
from cars.models import CarModel
from brands.models import BrandModel
from django.views.generic.list import ListView

def Home(request):
    cars = CarModel.objects.all()
    brands = BrandModel.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brands': brands})

class Branded(ListView):
    template_name = 'home.html'
    
    model = CarModel
    context_object_name = 'cars'
    def get_queryset(self):
        brand_slug = self.kwargs.get('brand_slug', 'ALL')
        if brand_slug != 'ALL':
            selected = BrandModel.objects.get(slug=brand_slug)
            return CarModel.objects.filter(brand=selected)
        else: return CarModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = BrandModel.objects.all()
        context['on_brand'] = self.kwargs.get('brand_slug', 'ALL')
        return context