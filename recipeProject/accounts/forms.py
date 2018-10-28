from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your email', max_length=200)
    password = forms.CharField(label='Your password', max_length=100, widget=forms.PasswordInput)


class LoginForm(forms.Form):
    name = forms.CharField(label='Your username', max_length=200)
    password = forms.CharField(label='Your password', max_length=100, widget=forms.PasswordInput)
