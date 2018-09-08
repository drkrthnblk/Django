# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
#added
from .models import Flight, Passenger
from django.urls import reverse

# Create your views here.
def index(request):
    #return HttpResponse("Flight!")f.origin.code
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
        "flight" : flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flights.html", context) 

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except Passenger.DoesNotExist:
        return render(request, "flight/error.html", {"message": "No passenger"})
    except Flight.DoesNotExist:
        return render(request, "flight/error.html", {"message": "No flight"})
    except KeyError:
        return render(request, "flight/error.html", {"message": "No selection"})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
    # reverse takes the name form urls and gets the relative url
   
