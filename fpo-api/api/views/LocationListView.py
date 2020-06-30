from rest_framework.request import Request
from rest_framework.response import Response
from api.serializers import LocationLookupSerializer
from api.models import Location
from rest_framework import generics


class LocationListView(generics.ListAPIView):
    queryset = ''

    def get(self, request: Request, *args, **kwargs):
        queryset = Location.objects.all()
        serializer = LocationLookupSerializer(queryset, many=True)
        return Response(serializer.data)
