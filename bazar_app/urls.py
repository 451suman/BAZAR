from django.urls import path

from bazar_app import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("product-list/", views.ProductsListView.as_view(), name="product-list")
]
