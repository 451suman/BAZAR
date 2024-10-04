from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
    FormView,
)

from bazar_app.models import Product

# Create your views here.
class AdminHomeView(TemplateView):
    template_name = 'admin/home/home.html'

class AdminProductsView(ListView):
    model = Product
    template_name = 'admin/product_list/product_list.html'
    context_object_name="products"
    paginate_by = 10

    def get_queryset(self):
        query = super().get_queryset()
        query = Product.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")
        return query