from django.contrib import admin
from . models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'user', 'image']
# same here.
# admin.site.register(Profile)