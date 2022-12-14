# Generated by Django 3.2.6 on 2021-09-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('dob', models.DateField()),
                ('gendar', models.CharField(max_length=55)),
                ('locality', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=55)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Assam', 'assam'), ('Delhi', 'delhi'), ('Goa', 'goa'), ('Usa', 'usa')], max_length=55)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=55)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profileimg')),
                ('my_file', models.ImageField(blank=True, upload_to='doc')),
            ],
        ),
    ]
