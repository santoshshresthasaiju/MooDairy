from django.urls import path
from .views import farmer_dashboard, admin_dashboard, user_list

app_name= 'dashboard'

urlpatterns = [
    path('dashboard/', admin_dashboard, name='dashboard'),
    path('farmer/', farmer_dashboard, name='farmer_dashboard'),
    
    path('user/list/', user_list, name='user_list'),
    
]
