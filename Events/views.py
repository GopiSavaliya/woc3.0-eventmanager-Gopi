from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
from .models import Participant
from twilio.rest import Client
import datetime

def eventdashboard(request):
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
        event.password = request.POST['hpass']
        event.save()
        return render(request, 'EventRegistration.html')
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
            account_sid = "AC1e260bb10ea3e3e096e9d346097c8005"
            auth_token = "527a9f5e5ae52b550144000ca09edd50"
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body="""\nThank you """ + participant.Name + """ for registering your participation with us.
    
    Participation ID:""" + str(participant.id) + """
    Event Name : """ + events.EventName + """
    Location : """ + events.Location + """
    Time : """ + str(events.From) + """-""" + str(events.To) + """"
    No. of people : """ + str(participant.NoOfPeople) + """
    
    -EventManager""",
                from_='+12139082091',
                to='+91' + participant.ContactNo
            )

        else:
            event['exist'] = "Participant already registered for the Event"

    return render(request, 'ParticipantReg.html', event)

