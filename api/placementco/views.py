from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from django.conf import settings 
from django.core.mail import send_mail
from api.feedback.models import Feedback

import random
import re
# Create your views here.

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'Send a Post request with parameter'})

    username = request.POST['email']
    password = request.POST['password']

    if not re.match("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", username):
        return JsonResponse({'error':'Enter a valid email'})

    if len(password) < 4:
        return JsonResponse({'error':'Password is too short write atleast 8 character'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != '0':
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':'Previous Session Exists!!'})

            token = generate_session_token()
            user.session_token = token
            user.save()

            login(request,user)
            return JsonResponse({'token':token,'user':usr_dict})
        
        else:
            return JsonResponse({'error':'Invalid Password!!!'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid email'})


def signout(request,id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid user ID'})

    return JsonResponse({'success':'Logged out Successfully!!'})

    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

@csrf_exempt
def send_message(request):
    email = request.POST['em']
    message = request.POST['message']
    sub = Feedback.objects.filter(email=email).values().first()
    subject = sub.pop("subject")

    send_mail('Hello, We are from Career Club', 
               'Here is answer of your inquiry '+subject +' , "'+message+'".', settings.EMAIL_HOST_USER, [email], fail_silently=False,)
    return JsonResponse({"success":"Sent Successfully!"})