from django.urls import path
from . import views

urlpatterns = [
	path('' , views.index, name = 'index'),
	path('searchflight/', views.searchFlight, name='searchFlight'),
	path('<int:accommodation_id>/accommodation', views.detailAccommodation, name='detailPage'),
	path('<int:attraction_id>/attraction', views.detailAttraction, name='detailPage'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote', views.vote, name = 'vote'),
# ]