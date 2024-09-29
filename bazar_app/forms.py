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


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile  # Make sure to import UserProfile


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=75, required=True)
    last_name = forms.CharField(max_length=75, required=True)
    password1 = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=200, required=True)
    phone = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "address",
            "phone",
        ]

    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            user.save()  # Save the User instance

            # Create UserProfile instance
            UserProfile.objects.create(
                user=user,
                address=self.cleaned_data["address"],
                phone=self.cleaned_data["phone"],
            )
        return user
