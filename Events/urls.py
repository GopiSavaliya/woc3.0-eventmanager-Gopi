from django.urls import path
from . import views

urlpatterns = [
    path('ParticipantReg/', views.participantreg),
    path('EventReg/', views.eventreg),
    path('EventDashboard/', views.eventdashboard),
]