from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from moodairy.models import Dairy, DairyUser
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
    try:
        # Get the DairyUser object related to the logged-in user
        dairy_user = DairyUser.objects.get(dairy_user=request.user)
        # Get the dairy related to this DairyUser
        user_dairy = dairy_user.dairy   
        # Get all CustomUser objects that have an associated DairyUser with the same dairy
        users = CustomUser.objects.filter(dairyuser__dairy=user_dairy)
        
        context = {
            'users': users,
        }
        return render(request, 'dashboard/user_list.html', context)
    
    except DairyUser.DoesNotExist:
        # If no DairyUser entry exists for the logged-in user, show a warning
        messages.warning(request, 'You are not assigned to a dairy. Please contact the admin.')
        return render(request, 'dashboard/user_list.html', {'users': []})
    
    except Dairy.DoesNotExist:
        # If no Dairy is assigned to the DairyUser, show a warning
        messages.warning(request, 'No dairy assigned to your user.')
        return render(request, 'dashboard/user_list.html', {'users': []})