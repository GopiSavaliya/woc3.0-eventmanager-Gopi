from django.contrib import admin
from .models import Event
from .models import Participant


admin.site.register(Event)
admin.site.register(Participant)
