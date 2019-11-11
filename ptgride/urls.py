from django.urls import path
from . import views

app_name = 'ptgride'

urlpatterns = [
    path('<int:user_id>/', views.index, name='index'),
    path('<int:user_id>/book', views.book, name = 'book')
]