from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    resumes = models.Resume.objects.all()
    context = {
        'resume': resumes,
    
    }
    return render(request, 'index.html',context)