from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def admin_dashboard(request):
    return render(request, 'registrations/admin_dashboard.html')

@login_required
def farmer_dashboard(request):
    return render(request, 'registrations/farmer_dashboard.html')

@login_required
def collector_dashboard(request):
    return render(request, 'registrations/collector_dashboard.html')

@login_required
def finance_dashboard(request):
    return render(request, 'registrations/finance_dashboard.html')

@login_required
def default_dashboard(request):
    return render(request, 'registrations/default_dashboard.html')