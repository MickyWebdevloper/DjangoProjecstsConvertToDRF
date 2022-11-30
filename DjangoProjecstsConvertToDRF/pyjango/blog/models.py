from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Post(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=55)
    content = HTMLField()
    code = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



