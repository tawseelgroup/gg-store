from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class salesDashboardView(TemplateView):
    template_name = 'sales_dashboard.html'
