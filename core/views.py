from django.shortcuts import render
from . models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

@login_required
def home(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    
    return render (request, 'core/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-posted_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):

    return render (request, 'core/about.html')
