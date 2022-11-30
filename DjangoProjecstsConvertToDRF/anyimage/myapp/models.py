from django.db import models

# Create your models here.

STATE_CHOICE = (
    ('Assam','assam'),
    ('Delhi','delhi'),
    ('Goa','goa'),
    ('Usa','usa')
)



class Resume(models.Model):
    name = models.CharField(max_length=55)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gendar = models.CharField(max_length=55)
    locality = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices= STATE_CHOICE, max_length=55)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=55)
    profile_picture = models.ImageField(upload_to='profileimg')
    my_file = models.FileField(upload_to='doc')

