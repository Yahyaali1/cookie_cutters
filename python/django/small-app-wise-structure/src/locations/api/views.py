from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .serializers import LocationSerializer
from ..models import Location


class LocationsView(ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationDetailView(RetrieveAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
