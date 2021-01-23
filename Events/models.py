from django.db import models


class Event(models.Model):
    EventName = models.CharField(max_length=50)
    EventPoster = models.CharField(max_length=255, default="C:/Users/Gopi/OneDrive/Documents/Projects/EventManagement/static/images/DefaultEventPoster.jpg")
    Description = models.CharField(max_length=300)
    Location = models.CharField(max_length=30)
    From = models.DateTimeField()
    To = models.DateTimeField()
    RegDeadline = models.DateTimeField()
    Email = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
