from rest_framework import viewsets
from .serializers import CompanyJobSerializer
from .models import CompanyJob
from api.companyhr.models import CompanyHr
from django.conf import settings 
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from api.student.models import Student
from django.http import JsonResponse

# Create your views here.

class CompanyJobViewSet(viewsets.ModelViewSet):
    queryset = CompanyJob.objects.all().order_by('id')
    serializer_class = CompanyJobSerializer 

    def perform_create(self, serializer):
        stud = Student.objects.filter(status=1).values('email')

        created_object = serializer.save()
        comp = CompanyHr.objects.filter(fullname=created_object.company).values().first()
        company = comp.pop("companyname")
        email = comp.pop("email")
        """ em = []
        for i in stud:
            em.append(i["email"]) """
        
        for i in stud:
            send_mail('1 new job for '+created_object.requirement+'!!',
                    f'Hello, See new job requirement is their for the position of '+created_object.requirement+' at '+
                    company+'. Contact to HR team at '+email+' for more details.',
                    settings.EMAIL_HOST_USER, 
                    [i["email"], ],  
                    fail_silently=False,)

        """ send_mail('1 new job for '+created_object.requirement+'!!',
                    f'Hello, See new job requirement is their for the position '+created_object.requirement+' at '+
                    company+'. Contact to HR team at '+email+' for more details.',
                    settings.EMAIL_HOST_USER, 
                    em,  
                    fail_silently=False,) """

        return JsonResponse({"success":"Email Sent successfully!"})