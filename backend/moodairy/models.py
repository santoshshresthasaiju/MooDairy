from django.db import models
from django.conf import settings

# Create your models here.
class Dairy(models.Model):
    dairy_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return self.dairy_name

class DairyUser(models.Model):
    dairy = models.ForeignKey(Dairy, on_delete=models.CASCADE)
    dairy_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.dairy_user.username
    

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Subscription(models.Model):
    dairy = models.OneToOneField(Dairy, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)