from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from . forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}! you are now able to login')
            return redirect('login')

# loginrequiredmixin
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form':u_form,
            'p_form':p_form,
        }
        return render(request, 'users/profile.html', context)
    
    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'{request.user} Porfile Updated Successfully!')
            return redirect('profile')