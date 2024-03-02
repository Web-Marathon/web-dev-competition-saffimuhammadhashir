# events/admin.py

from django.contrib import admin
from .models import CalendarEvent, RSVP

admin.site.register(CalendarEvent)
admin.site.register(RSVP)
