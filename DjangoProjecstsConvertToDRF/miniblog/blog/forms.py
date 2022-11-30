# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
# from django.db.models import fields
# from django.forms import widgets
# # from django.db.models import fields
# # from django.forms import widgets
# from django.utils.translation import gettext, gettext_lazy as _
# from django.contrib.auth.models import User
# from django import forms
# from .models import Contect, Post


# class SignupForm(UserCreationForm):
#     password1 = forms.CharField(
#         label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(
#         label='Confirm Password (Again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'})
#         }
#     pass


# class LoginForm(AuthenticationForm):
#     username = UsernameField(
#         widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
#     password = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
#     )


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'desc')
#         lebels = {'title': 'Title', 'desc': 'Description'}
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'desc': forms.Textarea(attrs={'class': 'form-control'})
#         }

# class ContectForm(forms.ModelForm):
#     class Meta:
#         model = Contect
#         fields = ('name','email','phone_num','context')
#         widgets = {
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'email':forms.EmailInput(attrs={'class':'form-control'}),
#             'phone_num':forms.NumberInput(attrs={'class':'form-control'}),
#             'context':forms.Textarea(attrs={'class':'form-control'})
#         }