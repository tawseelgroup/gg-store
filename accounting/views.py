from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class AccountingDashboardView(TemplateView):
    template_name = 'accounting_dashboard.html'


