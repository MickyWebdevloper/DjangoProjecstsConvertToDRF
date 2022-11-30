# from django.contrib import admin
# from django.db import models
# from . models import Post, Contect
'''
# Register your models here.
@admin.register(Post, Contect)
class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post, Contect
        fieldsets = (
            (None, {
                "fields": (
                    'id', 'title','desc'
                ),
            }),
        )
        '''
        
from django.contrib import admin
from .models import Post, Contact


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'date_posted']
    # pass


@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'content','phone_num']
