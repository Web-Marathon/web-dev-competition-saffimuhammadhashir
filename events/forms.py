# events/forms.py

from django import forms
from .models import CalendarEvent, RSVP

class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ['event_date', 'name', 'description']

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = []
