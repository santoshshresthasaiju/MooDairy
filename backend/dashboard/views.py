from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

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