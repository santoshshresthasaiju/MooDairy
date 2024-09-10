from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm , UserChangeForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2', 'role']
        
class CustomerUserChangeForm(UserChangeForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['username' , 'email', 'role']
        
class CustomLoginForm(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True, label="Role")
    
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if self.cleaned_data['role'] != user.role:
            raise forms.ValidationError(
                f"Invalid role for the user. Expected role: {user.role}.",
                code='invalid_role'
            )
            
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        role =self.cleaned_data.get('role')
        if username and password:
            self.user_cache = authenticate(self.request, username=username , password=password , role=role)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                if self.user_cache.role != role:
                    raise forms.ValidationError(f"The role provided does not match the user's role.")
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data