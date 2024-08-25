from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import CustomUser
from .serializers import UserSerializer

# Registration View (open to anyone)
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# Admin-only view
class AdminOnlyView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# Farmer-only view
class FarmerOnlyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        farmers = CustomUser.objects.filter(role='farmer')
        serializer = UserSerializer(farmers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# Collector-only view
class CollectorOnlyView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(role='collector')

# Finance Manager-only view
class FinanceManagerOnlyView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(role='finance_manager')
