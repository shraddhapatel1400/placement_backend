from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import CompanyHrSerializer
from .models import CompanyHr
from django.http import JsonResponse, HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password, make_password
from django.conf import settings 
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from api.student.models import Student
from api.companyhr.cmpJob.models import CompanyJob
from api.placementco.models import User
from twilio.rest import Client
from twilio.rest import TwilioRestClient

import datetime
import random
import re

# Create your views here.
def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'Send a Post request with parameter'})

    email = request.POST['email']
    password = request.POST['password']
    
    if email is not None :
        if not re.match("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", email):
            return JsonResponse({'error':'Enter a valid email'})
    else : 
        return JsonResponse({'error': 'Please provide your email'})

    if password is None :
        return JsonResponse({'error': 'Please provide your password'})

    try:
        user = CompanyHr.objects.get(email=email)

        if check_password(password,user.password) :
            usr_dict = CompanyHr.objects.filter(email=email).values().first()
            usr_dict.pop('password')

            if user.session_token != '0':
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':'You are already logged in!!'})

            token = generate_session_token()
            user.session_token = token
            user.save()

            login(request,user)
            return JsonResponse({'token':token,'user':usr_dict})
        else :
            return JsonResponse({'error': 'Invalid Password!'})

    except CompanyHr.DoesNotExist:
        return JsonResponse({'error':'Invalid email'})


def signout(request,id):
    logout(request)

    try:
        user = CompanyHr.objects.get(pk=id)
        user.session_token = "0"
        user.last_login = datetime.datetime.now()
        user.save()

    except CompanyHr.DoesNotExist:
        return JsonResponse({'error':'Invalid user ID'})

    return JsonResponse({'success':'Logged out Successfully!!'})


class CompanyHrViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = CompanyHr.objects.all().order_by('id')
    serializer_class = CompanyHrSerializer

    def perform_create(self, serializer):
        created_object = serializer.save()
        send_mail('Welcome to Career Club!!',
                    f'Hi {created_object.fullname}, Thank you for registering in Career Club.',
                    settings.EMAIL_HOST_USER, 
                    [created_object.email],  
                    fail_silently=False,)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


def confirm_mail(request,id,jid,cid):

    stud = Student.objects.filter(pk=id).values().first()
    job = CompanyJob.objects.filter(pk=jid).values().first()
    company = CompanyHr.objects.filter(pk=cid).values().first()

    firstname = stud.pop('firstname')
    lastname = stud.pop('lastname')
    email = stud.pop('email')
    phone = stud.pop('phone')

    requirement = job.pop('requirement')
    companyname = company.pop('companyname')

    send_mail('Congratulations!! '+ firstname +' '+ lastname,
              f'Hi {firstname} {lastname}, We are glad to inform you that you are selected for '
                +requirement+' in our company '+companyname+'. We are get back to you soon.',
              settings.EMAIL_HOST_USER, 
              [email],  
              fail_silently=False,)

    """ account_sid = "ACd39a211a29342a6b60e824cc9bb87068"
    auth_token  = "d0c41f8df38f987abf485bb8f052042f"
    message_to_broadcast = ("Congratulations!! "+firstname+" "+lastname+", We are glad to inform you that you are selected for "
                +requirement+' in our company '+companyname+'.')
    client = Client(account_sid, auth_token)
    sms = client.messages.create(
            body=message_to_broadcast,
            to="+91"+phone,
            from_="+17696100027") """
    return JsonResponse({'success':'Message sent successfully!'})


def reject_mail(request,id,jid,cid):

    stud = Student.objects.filter(pk=id).values().first()
    job = CompanyJob.objects.filter(pk=jid).values().first()
    company = CompanyHr.objects.filter(pk=cid).values().first()

    firstname = stud.pop('firstname')
    lastname = stud.pop('lastname')
    email = stud.pop('email')
    phone = stud.pop('phone')

    requirement = job.pop('requirement')
    companyname = company.pop('companyname')

    send_mail('Oops! Sorry '+ firstname +' '+ lastname,
              f'Hi {firstname} {lastname}, We are sorry to inform you that you are rejected for '
                +requirement+' in our company '+companyname+'.',
              settings.EMAIL_HOST_USER, 
              [email],  
              fail_silently=False,)

    """ account_sid = "ACd39a211a29342a6b60e824cc9bb87068"
    auth_token  = "d0c41f8df38f987abf485bb8f052042f"
    message_to_broadcast = ('Oops! Sorry '+ firstname +' '+ lastname+", We are sorry to inform you that you are rejected for "
                +requirement+' in our company '+companyname+'.')
    client = Client(account_sid, auth_token)
    sms = client.messages.create(
            body=message_to_broadcast,
            to="+91"+phone,
            from_="+17696100027") """

    return JsonResponse({'success':'Message sent successfully!'})


@csrf_exempt
def send_new_mail(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'Send a Post request with parameter'})

    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    image = request.FILES['image']
    
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    mail.attach(image.name, image.read(), image.content_type)
    mail.send()
    
    
    """  else :
        return JsonResponse({'email': 'Without image'})
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False,) """

    return JsonResponse({'email': 'Email Sent Successfully!'})


@csrf_exempt   
def invite_mail(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'Send a Post request with parameter'})

    pc = User.objects.values().first()
    pc_email = pc.pop('email')
    pc_phone = pc.pop('phone')
    email = request.POST['email']

    send_mail('Invitation From College of AIT.', 
                f"Hello, I'm Placement Co-ordinator at College of Agricultural Information Technology, "+
                "Anand Agricultural University, Anand. I'm Inviting you to visit our Campus. "+
                "We have best employee as our students. Feel free to contact me at my email "+pc_email+" or phone "+pc_phone,
                settings.EMAIL_HOST_USER, 
                [email], 
                fail_silently=False,)
    return JsonResponse({"success":"Invitation Sent Successfully!"})


