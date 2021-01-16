from django.http import HttpResponse
from django.shortcuts import render


def eventreg(request):
    return render(request, 'EventRegistration.html')


def eventdashboard(request):
    return render(request, 'EventDashBoard.html')
