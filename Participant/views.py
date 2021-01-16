from django.http import HttpResponse
from django.shortcuts import render


def participantreg(request):
    return render(request, 'ParticipantReg.html')
