from django.shortcuts import render
from . models import Post
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    
    return render (request, 'core/home.html',context)

def about(request):

    return render (request, 'core/about.html')
