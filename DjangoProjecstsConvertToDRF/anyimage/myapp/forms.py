from django import forms
from django.forms.forms import Form
from . models import Resume


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

JOB_CITY_CHOICES = [
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Assam', 'Assam'),
    ('Arunachal', 'Arunachal'),
    ('Mumbai', 'Mumbai'),
    ('Guwahati', 'Guwahati')
]


class ResumeForm(forms.ModelForm):
    gendar = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(
        label='Prefered Job Locations', choices=JOB_CITY_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ('name', 'dob', 'gendar', 'locality', 'city', 'pin',
                  'state', 'mobile', 'email', 'job_city', 'profile_picture', 'my_file')
        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'pin': 'Pin Code',
            'mobile': 'Mobile No',
            'email': 'Email Id',
            'profile_picture': 'Profile Image',
            'my_file': 'Document'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id':'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'my_file': forms.FileInput(attrs={'class': 'form-control'})
        }
