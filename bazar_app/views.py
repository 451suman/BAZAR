from django.contrib import messages
from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)

from bazar_app.forms import AddProductForm
from bazar_app.models import Product


# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = "home/home.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"] = Product.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")[:3]

        context["products"] = Product.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")

        return context


class ProductsListView(ListView):
    model = Product
    template_name = "product_list/product_list.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        query = super().get_queryset()
        query = Product.objects.filter(published_at__isnull=False, status="active").order_by("-published_at")
        return query
    
class CategoriesListView(ListView):
    model = Product
    template_name = "product_list/product_list.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False,
            status="active",
            category__id=self.kwargs["cid"],
        ).order_by("-published_at")
        return query
    
class TagsListView(ListView):
    model = Product
    template_name = "product_list/product_list.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False,
            status="active",
            category__id=self.kwargs["tid"],
        ).order_by("-published_at")
        return query
    




class ProductDetailView(DetailView):
    model = Product
    template_name = "productDetailPage/product_detail_page.html"
    context_object_name = "product"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            published_at__isnull=False,
            status="active",
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object  # Get the current product
        context["extra_products"] = Product.objects.filter(
            category=product.category,  # Filter by the same category
            published_at__isnull=False,
            status="active",
        ).exclude(id=product.id).order_by("-published_at")[:6]  # Exclude the current product
        return context



class ProductAddView(CreateView):
    model = Product
    template_name = "addproducts.html"
    form_class = AddProductForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Product added successfully!")
        return response
    
    def get_success_url(self):
        return reverse_lazy("product-detail", kwargs={"pk": self.object.pk})
    
class ProductUpdateView(UpdateView):
    model = Product
    template_name = "addproducts.html"
    form_class = AddProductForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Product Updated successfully!")
        return response
    
    def get_success_url(self):
        return reverse_lazy("product-detail", kwargs={"pk": self.object.pk})
    
