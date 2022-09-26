from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from .models import User


class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
