from django.forms import ValidationError
from django.shortcuts import get_object_or_404, render, redirect   
from django.contrib.auth import login, logout
from .models import OTP, CustomUser
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomerUserChangeForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from .utils import generate_otp
from django.contrib.auth import get_user_model
from .models import Dairy
    
User = get_user_model()

def landingpage_view(request):
    return render(request, 'registrations/landingpage.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.send_otp()  # Send OTP after user creation
            messages.success(request, "OTP sent to your email/phone. Verify to complete registration.")
            return redirect('registrations:otp-verify', user_id=user.id)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrations/signup.html', {'form': form})


def otp_verify_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)  # Ensure user exists

    if request.method == 'POST':
        otp_value = request.POST.get('otp')

        try:
            # Check if an OTP record exists for the user
            otp_record = OTP.objects.get(
                otp=otp_value, email=user.email
            )

            if otp_record.is_valid():
                # Activate the user upon successful OTP verification
                user.is_active = True
                user.save()

                otp_record.delete()  # Clean up OTP record
                messages.success(request, "Account verified! You can now log in.")
                return redirect('registrations:login')
            else:
                messages.error(request, "OTP has expired. Please request a new one.")
                return redirect('registrations:register')  # Optionally redirect to register

        except OTP.DoesNotExist:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'registrations/otp_verify.html', {'user_id': user_id})

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()

        if user:
            otp_value = generate_otp()
            OTP.objects.create(user=user, email=email, otp=otp_value)

            # Send OTP via email
            send_mail(
                'Password Reset OTP',
                f'Your OTP is: {otp_value}',
                'no-reply@example.com',
                [email],
            )
            messages.success(request, "OTP sent to your email. Please verify to reset your password.")
            return redirect('registrations:otp-verify-password', email=email)
        else:
            messages.error(request, "No user found with this email.")
    
    return render(request, 'registrations/password_reset_request.html')

def otp_verify_password(request, email):
    if request.method == 'POST':
        otp_value = request.POST.get('otp')

        try:
            otp_record = OTP.objects.get(otp=otp_value, email=email)

            if otp_record.is_valid():
                otp_record.delete()  # Clean up OTP record
                return redirect('registrations:password-reset-form', email=email)
            else:
                messages.error(request, "OTP has expired. Please request a new one.")
                return redirect('registrations:password-reset')

        except OTP.DoesNotExist:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'registrations/otp_verify_password.html', {'email': email})

def password_reset_form(request, email):
    user = get_object_or_404(User, email=email)

    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user.set_password(password)
            user.save()
            messages.success(request, "Password reset successfully! You can now log in.")
            return redirect('registrations:login')
        else:
            messages.error(request, "Passwords do not match. Please try again.")

    return render(request, 'registrations/password_reset_form.html', {'email': email})

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
            messages.success(request, 'Login successful!')
            # Check if the user has an assigned dairy
            if user.dairy:
                # If the user has a dairy assigned, proceed to the dashboard
                return redirect('dashboard:dashboard')
            else:
                # If no dairy is assigned, show a warning message
                messages.warning(request, 'No Dairy assigned to this user.')
        else:
            messages.error(request, 'Invalid username or password.') 
    else:
        form = CustomLoginForm()
    return render(request, 'registrations/login.html', {'form':form})

# def redirect_user_based_on_role(user):
#     if user.role == 'admin':
#         return redirect('dashboard:dashboard')
#     elif user.role == 'farmer':
#         return redirect(reverse('dashboard:farmer_dashboard'))
#     elif user.role == 'collector':
#         return redirect('dashboard:collector_dashboard')
#     elif user.role == 'finance_manager':
#         return redirect('dashboard:finance_dashboard')
#     else:
#         return redirect('dashboard:default_dashboard')
    
#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')
 