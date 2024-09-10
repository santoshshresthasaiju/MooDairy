from django.shortcuts import render, redirect   
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomerUserChangeForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
def dashboard(request):
    return render(request, 'registrations/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrations:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrations/register.html', {'form':form})

@login_required
def update_user(request):
    if request.method == 'POST':
        form = CustomerUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomerUserChangeForm(instance=request.user)
    return render(request, 'registrations/update_user.html', {'form': form})
        
def login_view(request):
    if request.method == 'POST':
        
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect_user_based_on_role(user)
        else:
            return render(request, 'registrations/login.html', {'form':form})
    else:
        form = CustomLoginForm()
    return render(request, 'registrations/login.html', {'form':form})

def redirect_user_based_on_role(user):
    if user.role == 'admin':
        return redirect('dashboard:admin_dashboard')
    elif user.role == 'farmer':
        return redirect('dashboard:farmer_dashboard')
    elif user.role == 'collector':
        return redirect('dashboard:collector_dashboard')
    elif user.role == 'finance_manager':
        return redirect('dashboard:finance_dashboard')
    else:
        return redirect('dashboard:default_dashboard')
    
