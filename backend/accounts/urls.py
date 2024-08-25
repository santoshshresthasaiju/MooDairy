from django.urls import path
from .views import UserRegisterView, AdminOnlyView, FarmerOnlyView, CollectorOnlyView, FinanceManagerOnlyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('admins/', AdminOnlyView.as_view(), name='admin-list'),
    path('farmer/', FarmerOnlyView.as_view(), name='farmer-list'),
    path('collector/', CollectorOnlyView.as_view(), name='collector-list'),
    path('finance-manager/', FinanceManagerOnlyView.as_view(), name='finance-manager-list'),
]
