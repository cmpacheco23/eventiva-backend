from datetime import datetime, timedelta, date
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Event(models.Model):
  class EventType(models.TextChoices):
    TRIP = 'Trip'
    ACTIVITY = 'ACTIVITY'
  name = models.CharField(max_length=150)
  startDate = models.DateField('Start Date', default=timezone.now)
  endDate = models.DateField('End Date', default=timezone.now() + timezone.timedelta(days=1))
  location = models.CharField(max_length=250)
  description = models.TextField
  event_type = models.CharField(
    max_length=20,
    choices=EventType.choices,
  )
  # need to add the poll embed
  # need to add the profile ref
  
class Trips(models.Model):
  # travelers = ref profile
  event = models.OneToOneField(Event, on_delete=models.CASCADE)
  def duration(self):
    if self.event.eventType == 'Trip':
      return (self.event.endDate - self.event.startDate).days
    else:
      return None