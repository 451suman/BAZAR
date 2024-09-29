from django.urls import path

from bazar_app import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("product-list/", views.ProductsListView.as_view(), name="product-list"),
    path("category-list/<int:cid>/", views.CategoriesListView.as_view(), name="category-list"),
    path("tag-list/<int:tid>/", views.TagsListView.as_view(), name="tag-list"),

    path("product-detail/<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("add-product/", views.ProductAddView.as_view(), name="add-product"),
    path("update-product/<int:pk>/", views.ProductUpdateView.as_view(), name="update-product"),
    path ("delete-product/<int:pk>/", views.ProductDeleteview.as_view(), name="delete-product"),

    path('register/', views.RegisterView.as_view(), name='register'),

    path("draft-product-list/", views.DraftProductsListView.as_view(), name="draft-product-list"),
    path("published/<int:id>/",views.PublishDraftView.as_view(), name="published"),

    path("category/", views.CategoryListView.as_view(), name="category"),
    path("tag/", views.TagListView.as_view(), name="tag"),
]
