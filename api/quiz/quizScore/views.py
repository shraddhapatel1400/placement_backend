from rest_framework import viewsets
from .serializers import QuizScoreSerializer
from .models import QuizScore

# Create your views here.

class QuizScoreViewSet(viewsets.ModelViewSet):
    queryset = QuizScore.objects.all().order_by('id')
    serializer_class = QuizScoreSerializer 
   