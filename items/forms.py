from django.contrib.auth import (authenticate,get_user_model,login,logout,)
from django import forms
from django.contrib.auth.models import User
from .models import user_table


class Userform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder' : 'enter username here'}),required=True,max_length=50)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder':'enter email here'}), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'enter password here'}),required=True,max_length=50)

    class Meta:
        model=user_table
        fields=('username','email',)
