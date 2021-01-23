from django.contrib import admin
from .models import Participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('Name', 'ContactNo', 'Email', 'EventName', 'RegType', 'NoOfPeople')


admin.site.register(Participant, ParticipantAdmin)
