from datetime import datetime, timedelta, date
from django.db import models
from django.utils import timezone
from django.urls import reverse
from appwrite.client import Client
from appwrite.services.users import Users

# Create your models here.

class Event(models.Model):
  class EventType(models.TextChoices):
    TRIP = 'Trip'
    ACTIVITY = 'Activity'
  name = models.CharField(max_length=150)
  startDate = models.DateField('Start Date', default=str(timezone.now))
  endDate = models.DateField('End Date', default= str(timezone.now() + timezone.timedelta(days=1)))
  location = models.CharField(max_length=250, default='')
  description = models.TextField
  event_type = models.CharField(
    max_length=20,
    choices=EventType.choices,
    default=EventType.TRIP,
  )
  # need to add the poll embed
  # need to add the profile ref
  
class Trips(models.Model):
  # travelers = ref profile
  event = models.OneToOneField(Event, on_delete=models.CASCADE)
  def duration(self):
    if self.event.event_type == 'Trip':
      return (self.event.endDate - self.event.startDate).days
    else:
      return None
    
class Poll(models.Model):
      event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='polls')
      pub_date = models.DateTimeField(auto_now_add=True)
      duration = models.CharField(max_length=10, choices=[('12hrs', '12 hours'), ('24hrs', '24 hours'), ('48hrs', '48 hours'), ('72hrs', '72 hours')])
      result = models.CharField(max_length=255)
      option1 = models.CharField(max_length=255, blank=True, null=True)
      option2 = models.CharField(max_length=255, blank=True, null=True)
      option3 = models.CharField(max_length=255, blank=True, null=True)
      option4 = models.CharField(max_length=255, blank=True, null=True)
      option5 = models.CharField(max_length=255, blank=True, null=True)
      option6 = models.CharField(max_length=255, blank=True, null=True)