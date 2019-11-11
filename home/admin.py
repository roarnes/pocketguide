from django.contrib import admin

from .models import Flight, Accommodation, Attraction

# Register your models here.
admin.site.register(Flight)
admin.site.register(Accommodation)
admin.site.register(Attraction)