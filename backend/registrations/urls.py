from django.urls import path 
from .views import register, update_user, dashboard, CustomLoginForm, login_view

app_name = 'registrations'

urlpatterns = [
    path('register/',register , name='register'),
    path('update/<int:pk>/', update_user, name='update_user'),
    path('',login_view, name='login')
]