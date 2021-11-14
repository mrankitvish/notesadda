from django.contrib.auth import models
from django.contrib.auth import forms
from django import forms
# from django import forms ##*
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class User_SignUp(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    password2=forms.CharField(label='Password Again',widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    class Meta:
        model=User
        fields={'username','first_name','last_name','email'}
        widgets={            
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),        
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
        } 

