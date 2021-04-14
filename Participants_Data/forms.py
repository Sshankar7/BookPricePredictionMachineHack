from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from .models import CustomUser
from django import forms
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class UserSignUpForm(CustomUserCreationForm):
    first_name = forms.CharField(
                    min_length  = 2,
                    max_length  = 100,
                    required    = True,
                    widget      = forms.TextInput(
                        attrs = {'class': 'form-control form-control-lg',
                        'placeholder': 'Enter your first name',
                        'type': 'text',
                        'autofocus': True}))

    last_name = forms.CharField(
                    min_length  = 2,
                    max_length  = 100,
                    required    = True,
                    widget      = forms.TextInput(
                        attrs={'class': 'form-control form-control-lg',
                        'placeholder': 'Enter your last name',
                        'type': 'text'}))
    
    mobile_number = forms.CharField(
                    max_length=10,
                    required=True,
                    widget=forms.TextInput(
                        attrs={'class':'form-control form-control-lg',
                        'placeholder':'Your 10 digit mobile number',
                        'type':'text',
                        'pattern': '^[1-9][0-9]{9}$'}))

    email = forms.EmailField(
                    max_length=254,
                    required=True,
                    widget=forms.TextInput(
                        attrs={'class': 'form-control form-control-lg',
                        'placeholder': 'Enter your email',
                        'type': 'email',
                        'autofocus': False}))

    password1 = forms.CharField(
                    max_length=100,
                    required=True,
                    widget=forms.PasswordInput(
                    attrs={'class': 'form-control form-control-lg',
                        'placeholder': 'Enter password',
                        'type': 'password'}))

    password2 = forms.CharField(
                    max_length=100,
                    required=True,
                    widget=forms.PasswordInput(
                    attrs={'class': 'form-control form-control-lg',
                        'placeholder': 'Confirm password',
                        'type': 'password'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'mobile_number', 'email', 'password1', 'password2', )


class UserPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
                        max_length=100,
                        required=True,
                        widget=forms.PasswordInput(
                        attrs={
                            'class': 'form-control form-control-lg',
                            'placeholder': 'Enter password',
                            'type': 'password',
                            'autofocus': True}))

    new_password2 = forms.CharField(
                        max_length=100,
                        required=True,
                        widget=forms.PasswordInput(
                        attrs={'class': 'form-control form-control-lg',
                        'placeholder': 'Confirm password',
                        'type': 'password'}))


class UserForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(
                max_length=254,
                required=True,
                widget=forms.TextInput(
                    attrs={'class': 'form-control form-control-lg',
                    'placeholder': 'Enter your email',
                    'type': 'email',
                    'autofocus': True}))