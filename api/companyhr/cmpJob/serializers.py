from rest_framework import serializers
from django.core.exceptions import ValidationError
import datetime

from .models import CompanyJob

class CompanyJobSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(CompanyJobSerializer, self).to_representation(instance)
        rep['company'] = instance.company.id
        rep['deadline'] = instance.deadline.strftime("%d-%b-%Y")
        return rep


    class Meta:
        model = CompanyJob
        fields = ('id','company','requirement','vacancy','jobtype','deadline')
