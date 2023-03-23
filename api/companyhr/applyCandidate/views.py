from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import ApplyJobSerializer
from .models import ApplyJob

# Create your views here.

class ApplyJobViewSet(viewsets.ModelViewSet):
    queryset = ApplyJob.objects.all().order_by('id')
    serializer_class = ApplyJobSerializer 
    permission_classes = [AllowAny]