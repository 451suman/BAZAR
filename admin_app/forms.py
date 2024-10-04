from django import forms
from bazar_app.models import Order, Product
from django_summernote.widgets import SummernoteWidget




class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ "title", "description", "featured_image", "video_link", "status", "category", "tag", "price", "stock"]
        widgets = {
            "description": SummernoteWidget(),
            "featured_image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),  # Optional customization
        }



class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =["ordered_status"]