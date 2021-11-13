from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from django.contrib import messages
from .models import Document
# Create your views here.

def Homeview(request):
    template_name='firstapp/Home.html'
    return render(request,template_name)

def Fileuploadview(request):
    template_name = 'firstapp/fileupload.html'
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url =  fs.url(filename)
        context = {'uploaded_file_url': uploaded_file_url}
        return render(request, template_name, context)
    return render(request, template_name)


def model_form_upload(request):
    template_name = 'firstapp/newfileupload.html'
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,'File is uploaded Successfullyy!!!...')
            return redirect('newfile')
    else:
        form = DocumentForm()
    context = {'form': form}
    return render(request, template_name, context)


def showfileview(request):
    file=Document.objects.all()
    template_name='firstapp/showfile.html'
    context={'file':file}
    return render(request,template_name,context)