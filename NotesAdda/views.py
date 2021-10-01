from django.shortcuts import redirect, render
from .models import uploadFiles
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request,'index.html/')
    	
def download(request):
   
    query_set=uploadFiles.objects.all()[:10]

    return render(request,'download.html/',{"uploadFiles":list(query_set)})

    	
    
def upload(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        uni_coll = request.POST['uni_coll']
        branchName = request.POST['branchName']
        year = request.POST['year']
        semName = request.POST['semName']
        myFile = request.FILES['myFile']   
        
        fs = FileSystemStorage()
        
        file = fs.save(myFile.name,myFile)     
        file_path = fs.url(file) 
        uploadFiles(name=name,email=email,uni_coll=uni_coll, branchName=branchName, year=year, semName=semName, myFile=myFile).save()
        return render(request, 'upload.html/', {'file_path': file_path}) 
    
    return render(request, 'upload.html/',{'notUploaded':'Fill the form to upload a file!'}) 
    
    
        


