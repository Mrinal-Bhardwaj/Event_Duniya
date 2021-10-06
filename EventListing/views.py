from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from .models import Contact, Event, About


def home(request):
    all_events = Event.objects.all()[:4]
    all = {
        'all_events': all_events,
    }
    return render(request, "home.html", all)


def about(request):
    about = About.objects.all()
    all = {
        'about': about,
    }
    return render(request, "about.html", all)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, query=desc)
        contact.save()
        messages.success(request, "Thank You ! We will reach you back soon")

    return render(request, "contact.html",{})


def alllist(request):
    all_events = Event.objects.all()
    all = {
        'all_events': all_events,
    }
    return render(request, "alllist.html", all)


def search(request):
    query = request.GET['search']
    search_event_name = Event.objects.filter(Name_of_event__icontains=query)
    search_location = Event.objects.filter(location__icontains=query)
    search_venue = Event.objects.filter(venue__icontains=query)
    search_industry = Event.objects.filter(industry__icontains=query)
    search_organizer = Event.objects.filter(organizer__icontains=query)
    search_type = search_organizer = Event.objects.filter(
        type_of_event__icontains=query)
    search_event = search_event_name.union(
        search_location, search_venue, search_industry, search_organizer, search_type)

    result = {
        'search_event': search_event
    }
    return render(request, "search.html", result)


def postanevent(request):
    if request.method == 'POST':
        event = Event()
        event.Name_of_event = request.POST.get('nameofevent', '')
        event.location = request.POST.get('eventlocation', '')
        event.duration = request.POST.get('durationofevent', '')
        event.time = request.POST.get('eventtime', '')
        event.venue = request.POST.get('eventvenue', '')
        event.industry = request.POST.get('eventindustry', '')
        event.organizer = request.POST.get('eventorganizer', '')
        event.link_to_register = request.POST.get('eventlink', '')
        event.type_of_event = request.POST.get('typeofevent', '')
        if len(request.FILES) != 0:
            event.pic_or_logo = request.FILES['eventposter']
        event.save()
        messages.success(
            request, "Thank You ! Your event will be posted as soon as verified :-)")

    return render(request, 'postanevent.html',{})


# def delete_event(request,event_id):
#     event = Event.objects.get(pk=event_id)
#     event.delete()
#     return redirect('alllist.html')