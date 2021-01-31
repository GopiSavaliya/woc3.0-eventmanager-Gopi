from argon2 import PasswordHasher
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
from .models import Participant
import datetime
#import smtplib
#from twilio.rest import Client


def eventdashboard(request):
    if request.method == 'POST':
        try:
            events = Event.objects.get(id=request.POST['EventID'])
        except:
            messages.warning(request, 'Please Enter Correct EventID')
            return render(request, 'EventDashBoard.html')

        if events.loginchk(request.POST['pass']):
            participants = Participant.objects.filter(EventName=events.EventName)
            data = {
                "participant": participants,
                "EventName": events.EventName
            }
            return render(request, 'EventDashBoard.html', data)
        else:
            messages.warning(request, 'Please Enter Correct Password')
            return render(request, 'EventDashBoard.html')
    else:
        return render(request, 'EventDashBoard.html')


def eventreg(request):
    if request.method == 'POST':
        event = Event()
        event.EventName = request.POST['EName']
        event.EventPoster = request.FILES['Poster']
        event.Description = request.POST['Desc']
        event.Location = request.POST['Location']
        event.From = request.POST['From']
        event.To = request.POST['To']
        event.RegDeadline = request.POST['Deadline']
        event.Email = request.POST['Email']
        encpass = PasswordHasher().hash(request.POST['hpass'].encode('utf-8'))
        event.password = encpass
        event.save()
        #Email sending code
        messages.success(request, 'Event Registration Successful. Kindly Check Email!')
        return render(request, 'Home.html')
    else:
        return render(request, 'EventRegistration.html')


def participantreg(request):
    data = Event.objects.filter(RegDeadline__gte=datetime.datetime.now())
    event = {
        "event_data": data,
        "exist": ""
    }
    if request.method == 'POST':
        events = Event.objects.get(id=request.POST['Event'])
        participants = Participant.objects.all()
        flag = 0
        for p in participants:
            if p.Email == request.POST['Email'] and p.EventName == events.EventName:
                flag = 1
        if flag == 0:
            participant = Participant()
            participant.Name = request.POST['Name']
            participant.ContactNo = request.POST['ContactNo']
            participant.Email = request.POST['Email']
            participant.EventName = events.EventName
            participant.RegType = request.POST['Type']
            participant.NoOfPeople = request.POST['People']
            participant.save()
            #SMS Sending Code
            messages.success(request, 'Participant Registration Successful. Kindly Check SMS!')
            return render(request, 'Home.html')
        else:
            messages.warning(request, "Participant already registered for the Event")
            return render(request, 'ParticipantReg.html', event)

    return render(request, 'ParticipantReg.html', event)
