from rest_framework import routers
from django.urls import path,include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.QuizViewSet)

urlpatterns = [
    path('quizhome/', include(router.urls)),
    path('quizscore/',include('api.quiz.quizScore.urls'))
]