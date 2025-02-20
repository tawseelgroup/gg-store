from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class operationsView(TemplateView):
    template_name = 'operations.html'
