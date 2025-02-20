from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class purchaseHomeView(TemplateView):
    template_name = 'purchase-dashboard.html'
