from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control w-100',
            'id': 'form2Example1',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control w-100',
            'id': 'form2Example2',
        })


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control w-100',
            'id': 'username',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control w-100',
            'id': 'email',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control w-100',
            'id': 'password1',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control w-100',
            'id': 'password2',
        })
