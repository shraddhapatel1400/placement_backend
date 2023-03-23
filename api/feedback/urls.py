from rest_framework import routers
from django.urls import path,include

from . import views

router = routers.DefaultRouter()
router.register(r'feedback', views.FeedbackViewSet)
router.register(r'technology', views.TechnologyViewSet)

urlpatterns = router.urls