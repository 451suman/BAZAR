from django import forms
from bazar_app.models import Contact, Product
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "description": SummernoteWidget(),
            "featured_image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),  # Optional customization
        }



class UserRegistrationForm(UserCreationForm):  #inheric UserCreation Form form auth.models
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name',"last_name"]