from django.shortcuts import render
from .models import Resume


def index(request):
    resumes = Resume.objects.all()
    print(resumes)

    ctx = {
        'resumes': resumes
    }
    return render(request, 'index.html', ctx)
