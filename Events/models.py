from django.db import models
from argon2 import PasswordHasher


class Event(models.Model):
    EventName = models.CharField(max_length=50)
    EventPoster = models.ImageField(upload_to="EventPoster")
    Description = models.CharField(max_length=300)
    Location = models.CharField(max_length=30)
    From = models.DateTimeField()
    To = models.DateTimeField()
    RegDeadline = models.DateTimeField()
    Email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.EventName


    def loginchk(self, pas):
        try:
            return PasswordHasher().verify(self.password.encode('utf-8'), pas)
        except:
            return False


class Participant(models.Model):
    Name = models.CharField(max_length=30)
    ContactNo = models.CharField(max_length=10)
    Email = models.CharField(max_length=255)
    EventName = models.CharField(max_length=50)
    RegType = models.CharField(max_length=15)
    NoOfPeople = models.IntegerField()
    def __str__(self):
        return self.Email
