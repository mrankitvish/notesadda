from django.shortcuts import redirect, render
from django.views import generic
from .models import Files
from django.contrib import messages


# Create your views here.
def download(request):
    return render(request,'download.html')

def upload(request):
    return render(request,'upload.html')





class FileView(generic.ListView):
    model = Files
    template_name = 'download.html'
    context_object_name = 'files'
    paginate_by = 6

    def get_queryset(self):
    	return Files.objects.order_by('-id')



def uploadFile(request):
    if request.method == 'POST':
        filename = request.POST['filename']
        owner = request.POST['owner']
        pdf = request.FILES['pdf']
        cover = request.FILES['cover']

        a = Files(filename=filename, owner=owner, pdf=pdf, cover=cover)
        a.save()
        messages.success(request, 'Files Submitted successfully!')
        return redirect('files')
    else:
    	return render(request, 'upload.html')