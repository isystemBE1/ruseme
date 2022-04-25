from django.shortcuts import render
from person.models import About, Partner, Resume
from posts.models import Post
from .forms import GetInTouchForm


# Create your views here.


def home_view(request):
    resumes = Resume.objects.all()
    ctx = {
        'resumes': resumes,
    }
    return render(request, 'index.html', ctx)
