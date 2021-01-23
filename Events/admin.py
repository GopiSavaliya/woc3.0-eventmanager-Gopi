from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('EventName', 'EventPoster', 'Description', 'Location', 'From', 'To', 'RegDeadline', 'Email')


admin.site.register(Event, EventAdmin)
