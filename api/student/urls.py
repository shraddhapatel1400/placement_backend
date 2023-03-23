from rest_framework import routers
from django.urls import path,include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.StudentViewSet)

urlpatterns = [
    path('personal/', include(router.urls)),
    path('education/', include('api.student.education.urls')),
    path('skills/', include('api.student.skills.urls')),
    path('projects/', include('api.student.projects.urls')),
    path('job/', include('api.student.job.urls')),

    path('signin/', views.signin, name='signin'),
    path('signout/<int:id>/', views.signout, name='signout'),
    path('sendsms/', views.broadcast_sms, name='sendsms'),
    path('resetpass/', views.reset_password, name='resetpass'),
]