from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Flight, Accommodation, Attraction


def index(request):
    latest_accommodation_list = Accommodation.objects.order_by('price')[:5]
    latest_attraction_list = Attraction.objects.order_by('attraction_name')[:5]
    template = loader.get_template('home/index.html')

    context = {
        'latest_accommodation_list': latest_accommodation_list,
        'latest_attraction_list': latest_attraction_list,
    }
    
    return HttpResponse(template.render(context, request))

def searchFlight(request):
    search_flight_by_city = request.GET.get('search_flight_by_city')

    returned_flight_list = Flight.objects.filter(to_city__icontains = search_flight_by_city)
    
    template = loader.get_template('home/search_result.html')

    context = {
        'returned_flight_list': returned_flight_list,
    }
    
    return HttpResponse(template.render(context, request))



def detailAccommodation(request, accommodation_id):

    accommodation_detail = Accommodation.objects.filter(id = accommodation_id)
    print(accommodation_detail)

    template = loader.get_template('home/detail_page.html')

    context = {
        'accommodation_detail': accommodation_detail,
    }

    return HttpResponse(template.render(context, request))

def detailAttraction(request, attraction_id):

    attraction_detail = Attraction.objects.filter(id = attraction_id)

    template = loader.get_template('home/detail_page.html')

    context = {
        'attraction_detail': attraction_detail,
    }

    return HttpResponse(template.render(context, request))

# def results(request, question_id):
#     return HttpResponse("You're looking at the result of %s." % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're answering question %s." % question_id)