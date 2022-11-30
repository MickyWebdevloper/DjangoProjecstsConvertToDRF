from PIL import Image
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from . models import Post
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, UpdateView
    )
from django.urls import reverse_lazy

# listing all views at home page.
class HomeListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    paginate_by = 5  # if pagination is desired
    ordering = ['-date_posted']

# showing one specific views at home page.
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'detail'

# listing perticular user's posts
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'user_posts'
    paginate_by = 5

    # Dynamic filtering ( all explenation are there, those are behind)
    def get_queryset(self):
        self.username = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=self.username).order_by('-date_posted')
    
# creating one specific post specific user.
# loginrequiredmixin
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create_post.html'
    model = Post
    fields = ['title','content','code',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# loginrequiredmixin
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'blog/delete_post.html'
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
# updating one specific views at home page.
# login required 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'blog/update_post.html'
    model = Post
    fields = ['title','content','code',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False