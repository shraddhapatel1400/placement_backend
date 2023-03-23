from rest_framework import routers
from django.urls import path,include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.CompanyHrViewSet)

urlpatterns = [
    path('company/', include(router.urls)),
    path('companyJob/', include('api.companyhr.cmpJob.urls')),
    path('applyJob/', include('api.companyhr.applyCandidate.urls')),
    path('signin/', views.signin, name='signin'),
    path('signout/<int:id>/', views.signout, name='signout'),
    path('confirmmail/<int:id>/<int:jid>/<int:cid>/', views.confirm_mail, name='confirmmail'),
    path('rejectmail/<int:id>/<int:jid>/<int:cid>/', views.reject_mail, name='rejectmail'),
    path('sendmail/', views.send_new_mail, name='sendmail'),
    path('invitemail/', views.invite_mail, name='invitemail'),
    
]