from rest_framework import viewsets
from .serializers import EducationSerializer
from .models import Education

# Create your views here.

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by('id')
    serializer_class = EducationSerializer 
   