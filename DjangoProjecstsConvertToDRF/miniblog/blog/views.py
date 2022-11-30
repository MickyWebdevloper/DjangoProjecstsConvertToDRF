# from _typeshed import Self
# from django.contrib import messages
# # can delete these
# # from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import authenticate, login, logout
# from . forms import SignupForm, LoginForm, PostForm, ContectForm
# from . models import Post
# from django.contrib.auth.models import Group, User
# # Create your views here.

from django.shortcuts import render, HttpResponseRedirect
from . models import Post
# from . models import Contact
from users.forms import ContectForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/')
    else:
        form = ContectForm()
    return render(request, 'blog/contact.html', {'form': form})
