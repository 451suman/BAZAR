from django.contrib import messages

from django.shortcuts import redirect, render
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
    FormView,
)

from admin_app.forms import UpdateOrderForm
from bazar_app.models import Order, OrderItem, Product

from django.shortcuts import render, get_object_or_404

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
    
class AdminOrderItemListView(ListView):
    model = OrderItem
    template_name = "admin/orders/orders.html"
    context_object_name = "items"

    def get_queryset(self):
        return OrderItem.objects.all().order_by("-created_at")
    




class OrderItemDetailView(UpdateView):
    template_name = "admin/orders/orders_detail.html" 

    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(OrderItem, pk=pk)  # Safely get the item or return a 404
        form = UpdateOrderForm  # Create a form instance with the item
        return render(request, self.template_name, {"item": item, "form": form})  # Render the template

    def post(self, request, ipk, *args, **kwargs):
        item = get_object_or_404(Order, pk=ipk)  # Safely get the item or return a 404
        form = UpdateOrderForm(request.POST, instance=item)  # Create a form instance with POST data and the item instance

        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the changes to the database
            messages.success(request, "Ordered status updated successfully!")  # Add a success message
            return redirect('admin-orderitem-detail', pk=item.pk)  # Redirect to the same page or another page

        # If the form is not valid, render the same template with the form errors
        return render(request, self.template_name, {"item": item, "form": form})