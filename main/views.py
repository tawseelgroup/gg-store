from django.shortcuts import render
from django.views.generic.base import TemplateView 
from .models import Company
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'homepage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.all()
        return context
    
class MainPageView(TemplateView):
    template_name ='main.html'
    
    

