from django.db import models


class Participant(models.Model):
    Name = models.CharField(max_length=30)
    ContactNo = models.CharField(max_length=10)
    Email = models.CharField(max_length=255)
    EventName = models.CharField(max_length=50)
    RegType = models.CharField(max_length=15)
    NoOfPeople = models.IntegerField()
