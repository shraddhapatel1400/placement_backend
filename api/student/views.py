from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import StudentSerializer
from .models import Student
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
from django.core.mail import send_mail, EmailMessage  
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
        user = Student.objects.get(email=email)

        if check_password(password,user.password) :
            usr_dict = Student.objects.filter(email=email).values().first()
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

    except Student.DoesNotExist:
        return JsonResponse({'error':'Invalid email'})


def signout(request,id):
    logout(request)

    try:
        user = Student.objects.get(pk=id)
        user.session_token = "0"
        user.last_login = datetime.datetime.now()
        user.save()

    except Student.DoesNotExist:
        return JsonResponse({'error':'Invalid user ID'})

    return JsonResponse({'success':'Logged out Successfully!!'})

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        created_object = serializer.save()
        send_mail('Welcome to Career Club!!',
                    f'Hi {created_object.firstname}, Thank you for registering in Career Club.',
                    settings.EMAIL_HOST_USER, 
                    [created_object.email],  
                    fail_silently=False,)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


def generate_otp(length=4):
    return ''.join(random.SystemRandom().choice([str(i) for i in range(10)]) for _ in range(length))

c = generate_otp()
@csrf_exempt
def broadcast_sms(request):
    request.session['otp'] = c
    if request.POST.get('phone'):
        phone = request.POST["phone"]
        account_sid = "ACd39a211a29342a6b60e824cc9bb87068"
        auth_token  = "d0c41f8df38f987abf485bb8f052042f"
        message_to_broadcast = ("Hi there, your OTP for forgot Password is "+request.session['otp'])
        client = Client(account_sid, auth_token)
        sms = client.messages.create(
                body=message_to_broadcast,
                to="+91"+phone,
                from_="+17696100027")
        return JsonResponse({"success": "OTP Sent Successfully!"})
    if request.POST.get('otp'):
        receive = request.POST["otp"]
        if (receive == request.session['otp']):
            return JsonResponse({"success": "Match!"})
        else:
            return JsonResponse({"error": "Invalid OTP!"})
    
@csrf_exempt
def reset_password(request):
    email = request.POST["email"]

    send_mail('Reset Password',
              f'Hi there, Here is your reset Password link http://localhost:3000/forgotemail/',
              settings.EMAIL_HOST_USER, 
              [email],  
              fail_silently=False,)
    return JsonResponse({"success":"Email sent successfully!","email":email})

""" @csrf_exempt
def reg_sms(request):
    phone = '6355413848'
    account_sid = "ACd39a211a29342a6b60e824cc9bb87068"
    auth_token  = "d0c41f8df38f987abf485bb8f052042f"
    message_to_broadcast = ("Hi there, your OTP for forgot Password is ")
    client = Client(account_sid, auth_token)

    validation_request = client.validation_requests.create(
                                friendly_name='My Home Phone Number',
                                phone_number='+91'+phone
                            )
    print(validation_request.friendly_name)

    return JsonResponse({"success": "OTP Sent Successfully!"}) """
    

