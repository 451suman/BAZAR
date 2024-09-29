from django.contrib import messages

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
    FormView,
)

from bazar_app.forms import AddProductForm, UserRegistrationForm
from bazar_app.models import Category, Product, Tag
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
# from django.contrib.auth import login


# Create your views here.
class RegisterView(FormView):
    template_name = "registration/signup.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Signup Successfull!")
        # login(self.request, user)
        return super().form_valid(form)


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
        ).order_by("-published_at")[:8]

        return context


class ProductsListView(ListView):
    model = Product
    template_name = "product_list/product_list.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        query = super().get_queryset()
        query = Product.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")
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
            tag__id=self.kwargs["tid"],
        ).order_by("-published_at")
        return query


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "productDetailPage/product_detail_page.html"
    context_object_name = "product"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            
            status="active",
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object  # Get the current product
        context["extra_products"] = (
            Product.objects.filter(
                category=product.category,  # Filter by the same category
                published_at__isnull=False,
                status="active",
            )
            .exclude(id=product.id)
            .order_by("-published_at")[:6]
        )  # Exclude the current product
        return context


class ProductAddView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "forms/addproducts.html"
    form_class = AddProductForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Product added successfully!")
        return response

    def get_success_url(self):
        return reverse_lazy("product-detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "forms/addproducts.html"
    form_class = AddProductForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Product Updated successfully!")
        return response

    def get_success_url(self):
        return reverse_lazy("product-detail", kwargs={"pk": self.object.pk})


class ProductDeleteview(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("product-list")
    # success_url: This attribute defines the URL to redirect to after the Post has been successfully deleted.

    def form_valid(self, form):
        messages.success(self.request, "product was Deleted Successfully")
        return super().form_valid(form)


class DraftProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list/product_list.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        query = super().get_queryset()
        query = Product.objects.filter(
            published_at__isnull=True, status="active"
        ).order_by("-created_at")
        return query
    


class PublishDraftView(LoginRequiredMixin, View):
    def get(self, request, id):  # Change `pk` to `id` here
        product = Product.objects.get(pk=id, published_at__isnull=True)
        product.published_at = timezone.now()
        product.save()
        messages.success(request, "Product was published successfully!")
        return redirect("product-detail", id)



class CategoryListView(ListView):
    model = Category
    template_name = "category_name_list.html"
    context_object_name="categories"

class TagListView(ListView):
    model = Tag
    template_name = "tag_name_list.html"
    context_object_name="tags"