from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class inventoryDashboardView(TemplateView):
    template_name = 'inventory_dashboard.html'
