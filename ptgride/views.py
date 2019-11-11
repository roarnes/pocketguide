from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
import faker

from .models import PtgBooking, User, Location

def index(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    booking_list = user.ptgbooking_set.all().exclude(time_end__lte=timezone.now())
    location = Location.objects.all()
    context = {
        'booking_list': booking_list,
        'user': user,
        'location': location
    }
    return render(request, 'ptgride/index.html', context)

def book(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    booking_list = user.ptgbooking_set.all().exclude(time_end__lte=timezone.now())
    location = Location.objects.all()

    try:
        pickup_location = Location.objects.get(name=request.POST['pickup'])
        dropoff_location = Location.objects.get(name=request.POST['dropoff'])
    except (KeyError, Location.DoesNotExist):
        return render(request, 'ptgride/index.html', {
            'booking_list': booking_list,
            'user': user,
            'location': location,
            'error_message': "You didn't select a choice, or choice invalid.",
        })
    
    if (request.POST['choice'] == 'Ride'):
        type = 1
    else:
        type = 2

    print(request.POST['pickup'])

    booking = PtgBooking.objects.create(
        type=type,
        time_begin=timezone.now(),
        time_end=timezone.now() + timezone.timedelta(days=1),
        pickup_location=pickup_location,
        dropoff_location=dropoff_location,
        cost=faker.Faker().random.randint(10000, 25000),
        user = User.objects.get(id=user_id)       
    )

    return HttpResponseRedirect(reverse('ptgride:index', args=(user.id,)))