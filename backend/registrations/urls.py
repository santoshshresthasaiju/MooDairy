from django.urls import path 
from .views import register, update_user, login_view, landingpage_view, otp_verify_view
from . import views

app_name = 'registrations'

urlpatterns = [
    path('', landingpage_view, name='landingpage'),
    path('register/',register , name='register'),
    path('update/<int:pk>/', update_user, name='update_user'),
    path('login/',login_view, name='login'),
    path('logout', views.logoutuser, name="logout"),
    path('otp-verify/<int:user_id>/', otp_verify_view, name='otp-verify'),
    
    path('password-reset/', views.password_reset_request, name='password-reset'),
    path('otp-verify-password/<str:email>/', views.otp_verify_password, name='otp-verify-password'),
    path('reset-form/<str:email>/', views.password_reset_form, name='password-reset-form'),
    
]