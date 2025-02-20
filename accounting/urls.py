from django.urls import path
from . import views


app_name = 'accounting'
urlpatterns = [
    path('', views.AccountingDashboardView.as_view(), name='accountingDashboard'),
]