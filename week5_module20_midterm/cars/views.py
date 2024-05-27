from .models import CarModel
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from comments.forms import CommentForm

class CarDetails(DetailView):
    model = CarModel
    template_name = 'details.html'
    slug_url_kwarg = 'car_slug'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Car'] = self.object
        context['Comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = self.get_object()
            comment.save()
        return self.get(request, *args, **kwargs)