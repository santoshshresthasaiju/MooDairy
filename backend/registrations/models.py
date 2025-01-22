from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now, timedelta
from moodairy.models import Dairy

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Role name (e.g., Admin, Farmer, etc.)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='otps')
    otp = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        """Check if the OTP is still valid (within 10 minutes)."""
        return now() < self.created_at + timedelta(minutes=10)

    def __str__(self):
        return f"OTP for {self.user.username} - {self.otp}"
