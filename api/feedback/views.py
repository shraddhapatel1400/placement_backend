from rest_framework import viewsets
from .serializers import FeedbackSerializer, TechnologySerializer
from .models import Feedback, Technology

# Create your views here.

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('id')
    serializer_class = FeedbackSerializer 

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all().order_by('id')
    serializer_class = TechnologySerializer 
   

