from django.urls import path,include
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path('', home, name='home'),
    
    path('student/', include('api.student.urls')),
    path('companyhr/', include('api.companyhr.urls')),
    path('placementco/', include('api.placementco.urls')),
    path('quiz/', include('api.quiz.urls')),
    path('feedback/', include('api.feedback.urls')),

    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]