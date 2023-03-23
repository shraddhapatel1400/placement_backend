from rest_framework import viewsets
from .serializers import SkillSerializer
from .models import Skills

# Create your views here.

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all().order_by('id')
    serializer_class = SkillSerializer 
   