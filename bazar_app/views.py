from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView, DetailView

from bazar_app.models import Product
# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = 'home/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"] = Product.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")[:3]

        context["products"] = Product.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")

        return context