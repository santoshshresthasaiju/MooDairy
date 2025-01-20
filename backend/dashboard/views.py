from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from registrations.models import CustomUser 

# Create your views here.
@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def farmer_dashboard(request):
    return render(request, 'dashboard/farmer_dashboard.html')

@login_required
def collector_dashboard(request):
    return render(request, 'dashboard/collector_dashboard.html')

@login_required
def finance_dashboard(request):
    return render(request, 'dashboard/finance_dashboard.html')

@login_required
def default_dashboard(request):
    return render(request, 'dashboard/default_dashboard.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def user_list(request):
    users = CustomUser.objects.all()
    context ={
        'users':users,
    }
    return render(request, 'dashboard/user_list.html', context)

