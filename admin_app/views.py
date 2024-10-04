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

# Create your views here.
class AdminHomeView(TemplateView):
    template_name = 'admin/home/home.html'