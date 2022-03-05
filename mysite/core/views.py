from re import template
from unicodedata import name
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


@csrf_exempt
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)
