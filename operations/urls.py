from django.urls import path
from . import views

app_name = 'operations'
urlpatterns = [
    path('', views.operationsView.as_view(), name='operations'),
]
