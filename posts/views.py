from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
def index(request):

    return render(request, 'index.html')


def about(request):

    return render(request, 'about.html')


class PostView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'posts.html'

