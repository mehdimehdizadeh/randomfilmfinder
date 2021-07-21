from django import forms
from django.forms.widgets import PasswordInput

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label = "Username",widget=forms.TextInput(attrs = {'class':'user_class'}))
    password = forms.CharField(max_length=50,label = "Password",widget= forms.PasswordInput(attrs = {'class':'user_class'}))
    confirm = forms.CharField(max_length=50,label = "Confirm",widget= forms.PasswordInput(attrs = {'class':'user_class'}))
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm  and password != confirm:
            raise forms.ValidationError("Password is not correct!")
        values = {
            "username":username,
            "password":password,
        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,label = "Username",widget=forms.TextInput(attrs = {'class':'user_class'}))
    password = forms.CharField(max_length=50,label = "Password",widget= forms.PasswordInput(attrs = {'class':'user_class'}))