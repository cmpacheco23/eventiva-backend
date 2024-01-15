from datetime import datetime, timedelta, date
from django.db import models
from django.utils import timezone
from django.urls import reverse
from appwrite.client import Client
from appwrite.services.users import Users

# Create your models here.

class AppUser(models.Model):
  user_id = models.CharField(max_length=36, unique=True, primary_key=True)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=15)
  password = models.CharField(max_length=128)
  name = models.CharField(max_length=128)

  def __str__(self):
    return self.name

class Profile(models.Model):
  app_users = models.OneToOneField('AppUser', on_delete=models.CASCADE)
  avatar = models.ImageField(upload_to='profile_avatars/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Event(models.Model):
  class EventType(models.TextChoices):
    TRIP = 'Trip'
    ACTIVITY = 'Activity'
  name = models.CharField(max_length=150)
  start_date = models.DateField('Start Date', default=str(timezone.now))
  end_date = models.DateField('End Date', default= str(timezone.now() + timezone.timedelta(days=1)))
  location = models.CharField(max_length=250, default='')
  description = models.TextField()
  event_owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
  event_type = models.CharField(
    max_length=20,
    choices=EventType.choices,
    default=EventType.TRIP,
  )
  
class Trips(models.Model):
  # travelers = ref profile
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='trips')
  def duration(self):
    if self.event.event_type == 'Trip':
      return (self.event.end_date - self.event.start_date).days
    else:
      return None
    
class Poll(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='polls')
  pub_date = models.DateTimeField(auto_now_add=True)
  duration = models.CharField(max_length=10, choices=[('12hrs', '12 hours'), ('24hrs', '24 hours'), ('48hrs', '48 hours'), ('72hrs', '72 hours')])
  poll_result = models.CharField(max_length=255)
  option1 = models.CharField(max_length=255, blank=True, null=True)
  option2 = models.CharField(max_length=255, blank=True, null=True)
  option3 = models.CharField(max_length=255, blank=True, null=True)
  option4 = models.CharField(max_length=255, blank=True, null=True)
  option5 = models.CharField(max_length=255, blank=True, null=True)
  option6 = models.CharField(max_length=255, blank=True, null=True)

class Notes(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  author = models.ForeignKey(Profile, on_delete=models.CASCADE)
  def __str__(self):
      return self.title
  

