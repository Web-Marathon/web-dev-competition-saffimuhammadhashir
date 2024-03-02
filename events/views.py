# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CalendarEvent,RSVP
from .forms import CalendarEventForm

@login_required
def all_calendar_events(request):
    events = CalendarEvent.objects.all()
    return render(request, 'events/all_calendar_events.html', {'events': events})

@login_required
def create_calendar_event(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('all_calendar_events')
    else:
        form = CalendarEventForm()
    return render(request, 'events/create_calendar_event.html', {'form': form})

@login_required
def edit_calendar_event(request, slug):
    event = get_object_or_404(CalendarEvent, slug=slug)
    if request.method == 'POST':
        form = CalendarEventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('all_calendar_events')
    else:
        form = CalendarEventForm(instance=event)
    return render(request, 'events/edit_calendar_event.html', {'form': form, 'event': event})

from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CalendarEvent, RSVP


@login_required
def event_detail(request, slug):
    event = get_object_or_404(CalendarEvent, slug=slug)
    rsvp_count = RSVP.objects.filter(event=event).count()
    user_rsvped = RSVP.objects.filter(event=event, user=request.user).exists()

    if request.method == 'POST':
        if 'rsvp' in request.POST:
            if not user_rsvped:
                rsvp = RSVP(user=request.user, event=event)
                rsvp.save()
                messages.success(request, 'You have successfully RSVP\'d for the event.')
        elif 'unrsvp' in request.POST:
            if user_rsvped:
                RSVP.objects.filter(user=request.user, event=event).delete()
                messages.success(request, 'You have successfully un-RSVP\'d for the event.')

    return render(request, 'events/event_detail.html', {'event': event, 'rsvp_count': rsvp_count, 'user_rsvped': user_rsvped})


