from django.shortcuts import render
from person.models import About, Partner
from posts.models import Post
from .forms import GetInTouchForm

# Create your views here.


def home_view(request):
    obj = About.objects.order_by('-id')[:1]
    partner = Partner.objects.all()
    post = Post.objects.order_by('-id')
    form = GetInTouchForm(request.POST or None)
    if form.is_valid():
        form.save()
    ctx = {
        'objects': obj,
        'partners': partner,
        'posts': post,
        'form': form
    }
    return render(request, 'index.html', ctx)
