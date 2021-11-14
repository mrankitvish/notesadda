from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def download(re):
    return HttpResponseRedirect('/notes/download/')
def upload(re):
    return HttpResponseRedirect('/notes/upload/')