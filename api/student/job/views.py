from rest_framework import viewsets
from .serializers import JobSerializer
from .models import Summary

# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Summary.objects.all().order_by('id')
    serializer_class = JobSerializer 
   