import re
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name', 'address', 'contact', 'pan', 'dob', 'gender', 
            'email', 'job_title', 'salary', 'hire_date', 'department', 
            'is_active', 'profile_picture'
        ]
        
        # Optional: Add widgets to customize form field appearances
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
            'is_active': forms.CheckboxInput(),
            'profile_picture': forms.ClearableFileInput(attrs={'multiple': True}),
        }

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        
        # Remove non-numeric characters (such as +, -, spaces)
        contact_cleaned = re.sub(r'\D', '', contact)  # Remove all non-numeric characters
        
        # Assuming the country code is included and the phone number should be 10 digits long after removing the country code
        # The country code can vary, so adjust the expected length accordingly
        if len(contact_cleaned) < 10:
            raise forms.ValidationError("Contact number must be at least 10 digits long, including country code.")
        
        return contact 