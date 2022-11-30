from django.contrib import admin
from . models import Resume
# Register your models here.


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'gendar', 'locality', 'city', 'pin',
                    'state', 'mobile', 'email', 'job_city', 'profile_picture', 'my_file']
