from django.urls import path 
from .views import register, update_user, login_view, landingpage_view

app_name = 'registrations'

urlpatterns = [
    path('', landingpage_view, name='landingpage'),
    path('register/',register , name='register'),
    path('update/<int:pk>/', update_user, name='update_user'),
    path('login/',login_view, name='login')
    
]