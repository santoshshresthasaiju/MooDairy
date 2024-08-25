from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
        ('collector', 'Collector'),
        ('finance_manager', 'Finance Manager'),
    )
       
       
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def __str__(self):
        return self.username
    
    
