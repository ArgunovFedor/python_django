import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_media.forms import UploadFileForm, DocumentForm, MultiFileForm
from app_media.models import File


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            File.objects.create(file=file, description='описание')
            return HttpResponse(content=file.name, status=200)
    else:
        upload_file_form = UploadFileForm()
    context = {
        'form': upload_file_form
    }
    return render(request, 'media/upload_file.html', context=context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'media/file_form_upload.html', {
        'form': form
    })


def upload_files(request):
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for file in files:
                instance = File(file=file)
                instance.save()
            return redirect('/')
    else:
        form = MultiFileForm()
    return render(request, 'media/upload_files.html', {'form': form})