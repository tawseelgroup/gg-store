from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AccountsView(TemplateView):
    template_name = 'accounts.html'


