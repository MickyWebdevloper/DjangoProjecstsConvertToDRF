from django.contrib import admin
from . models import Profile


@admin.register(Profile)
class ProfiileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image']
