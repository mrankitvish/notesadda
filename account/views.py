from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponseRedirect
from .forms import User_SignUp
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.

def usignup(re):
    if re.method=='POST':
        fm=User_SignUp(re.POST)
        if fm.is_valid():
            fm.save()
            messages.success(re,'Account has been created successfully!!')
            return HttpResponseRedirect('/')
        else:                                           
            return render(re,'signup.html',{'form':fm})       ###############################
                                                               #this is right way to show error
                                                              ###############################
    fm=User_SignUp()
    return render(re,'signup.html',{'form':fm})

def ulogin(request):
    if not request.user.is_authenticated: #user can't access login page, if they are loggedIn
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname, password=upass) #if user is created it returns UserObject, otherwise None
                if user is not None:
                    messages.success(request,'Successfully loggedIn!')
                    login(request, user)
                    return HttpResponseRedirect('/account/login/')
                else:
                    messages.info(request,'Username Not Found!')
            else:
                messages.error(request,'Invalid Username or Password!!')
                return render(request,'login.html',{'form':fm})    
        fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    return HttpResponseRedirect('/') #authomatically user will go on profile page


def ulogout(re):
    logout(re)
    messages.warning(re,'LoggedOut!')
    return  HttpResponseRedirect('/')



