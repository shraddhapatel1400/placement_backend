from rest_framework import viewsets
from .serializers import QuizSerializer
from .models import Quiz

# Create your views here.

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all().order_by('id')
    serializer_class = QuizSerializer 
   