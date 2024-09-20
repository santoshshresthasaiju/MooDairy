from django.urls import path
from .views import farmer_dashboard, dashboard

app_name= 'dashboard'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('farmer/', farmer_dashboard, name='farmer_dashboard'),
    
]
