from django.shortcuts import render
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from icalendar import Event as iCalEvent, Calendar

@login_required
def events(request):
    events = Event.objects.all()

    return render(request, 'events.html', {'events':events})

@login_required
def join_event(request):

    if request.method == 'POST':
        
        event_id = request.POST.get('event_id')
        event = get_object_or_404(Event, pk=event_id)


        cal = Calendar()
        ical_event = iCalEvent()
        ical_event.add('title', event.event_name)
        ical_event.add('start', event.event_date)
        ical_event.add('end', event.event_date)
        ical_event.add('location', event.venue)
        ical_event.add('description', event.event_details)
        cal.add_component(ical_event)
        response = HttpResponse(cal.to_ical(), content_type = 'text/calendar')
        response['Description'] = f'atachment; filename ="{event.event_name}.ics"'

        return response
    else:
        return HttpResponse('Method not allowed', status = 405)
    




