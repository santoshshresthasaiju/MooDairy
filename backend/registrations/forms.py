from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, OTP
from registrations.utils import generate_otp, send_otp_email, send_otp_sms


class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    otp = forms.IntegerField(
        required=False, help_text="Enter the OTP sent to your email or phone."
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2', 'role']

    def save(self, commit=True):
        """Save user but keep inactive until OTP verification."""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.role = self.cleaned_data['role']
        user.is_active = False  # Set inactive until OTP verification

        if commit:
            user.save()
        return user

    def send_otp(self):
        """Generate and send OTP to email and/or phone."""
        otp_value = generate_otp()
        OTP.objects.create(
            user=self.instance,  # Ensure OTP is linked to the created user
            otp=otp_value,
            email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'],
        )

        # Send OTP to email and phone
        send_otp_email(self.cleaned_data['email'], otp_value)
        send_otp_sms(self.cleaned_data['phone_number'], otp_value)


class CustomerUserChangeForm(UserChangeForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role']


class CustomLoginForm(AuthenticationForm):
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES, required=True, label="Role"
    )

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if self.cleaned_data['role'] != user.role:
            raise forms.ValidationError(
                f"Invalid role for the user. Expected role: {user.role}.",
                code='invalid_role',
            )

    def clean(self):
        """Override clean to add role-based authentication."""
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        role = self.cleaned_data.get('role')

        if username and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            elif self.user_cache.role != role:
                raise forms.ValidationError(
                    f"The role provided does not match the user's role."
                )
            self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
