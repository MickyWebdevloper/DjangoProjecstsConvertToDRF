from . models import Image
from django import forms


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':''}
