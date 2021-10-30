from django.urls import path
from .views import LocationsView, LocationDetailView

urlpatterns = [
    path('', LocationsView.as_view()),
    path('<int:pk>', LocationDetailView.as_view())
]
