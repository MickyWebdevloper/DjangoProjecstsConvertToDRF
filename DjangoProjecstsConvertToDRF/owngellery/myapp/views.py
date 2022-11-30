from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from . models import Image
from . forms import ImageUploadForm
# Create your views here.


def home(request):
    if request.method == 'POST':
        fm = ImageUploadForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    fm = ImageUploadForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'form': fm, 'images': img})
