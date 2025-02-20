from django.urls import path
from . import views


app_name = 'inventory'
urlpatterns = [
    path('', views.inventoryDashboardView.as_view(), name='inventoryDashboard'),
]