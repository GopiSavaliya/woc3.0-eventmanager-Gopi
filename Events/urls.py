from django.urls import path
from . import views

urlpatterns = [
    path('EventReg/', views.eventreg),
    path('EventDashboard/', views.eventdashboard),
]