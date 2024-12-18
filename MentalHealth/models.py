# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class CustomUser(models.Model):

    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    

    username = models.CharField(max_length=255)
    password= models.CharField(max_length=255)

    email = models.EmailField(max_length=255)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='user')
    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.user.username
    
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(Profile, related_name='created_events', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Resource(models.Model):
    CATEGORIES = [
        ('Mental Health', 'Mental Health'),
        ('Stress Management', 'Stress Management'),
        ('Self Care', 'Self Care'),
        ('Motivation', 'Motivation'),
        ('Eating Disorders', 'Eating disorders'),
        ('Anxiety', 'Anxiety disorders'),
        ('Dipression', 'Depression'),



    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORIES)
    uploader = models.ForeignKey(Profile, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Like(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 


class Appointment(models.Model):
    SLOT_CHOICES = (
        ('9:00 AM - 10:00 AM', '9:00 AM - 10:00 AM'),
        ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
        ('11:00 AM - 12:00 PM', '11:00 AM - 12:00 PM'),
        ('1:00 PM - 2:00 PM', '1:00 PM - 2:00 PM'),
        ('2:00 PM - 3:00 PM', '2:00 PM - 3:00 PM'),
        ('3:00 PM - 4:00 PM', '3:00 PM - 4:00 PM'),
    )
    
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    slot = models.CharField(max_length=100, choices=SLOT_CHOICES)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.user} at {self.slot}"
    def clean(self):
        if self.date < timezone.now().date():
            raise ValidationError('Date must be a future date.')