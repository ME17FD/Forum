# forms.py
from django import forms
from .models import User
from django.core.exceptions import ValidationError



class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'fname', 'lname', 'phone','profile_pic', 'password']
        requied = User.REQUIRED_FIELDS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.Meta.requied:
            self.fields[field_name].required = True

        # Set default values for form fields
        
        


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Add custom password validation if needed
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

    def clean_profile_pic(self):
        profile_pic = self.cleaned_data.get('profile_pic')
        # Add custom validation for cin_image
        return profile_pic



    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user