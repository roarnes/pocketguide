from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('<int:user_id>/', views.index, name = 'index'),
]