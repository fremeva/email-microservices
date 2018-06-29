from django.shortcuts import render, redirect

# Create your views here.
from upload_file_app.forms import DocumentForm


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/uploadfile/')
    else:
        form = DocumentForm()
    return render(request, 'upload_file_app/upload.html', {
        'form': form
    })
