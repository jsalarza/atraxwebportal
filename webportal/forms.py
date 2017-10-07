from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(widget=forms.EmailInput, required=True , label='Email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'username', 'password', 'confirm_password']



