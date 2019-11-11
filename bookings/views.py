from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Booking, User
from datetime import datetime

def index(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    booking_list = user.booking_set.all().exclude(time_end__lte=datetime.now())
    context = {
        'booking_list': booking_list,
        'user': user,
    }
    return render(request, 'bookings/index.html', context)