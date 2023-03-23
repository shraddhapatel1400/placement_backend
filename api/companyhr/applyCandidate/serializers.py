from rest_framework import serializers
from django.core.exceptions import ValidationError
from datetime import datetime 
from django.utils import timezone

from .models import ApplyJob

""" class DateTimeTzAwareField(serializers.DateTimeField):
    def to_native(self, value):
        value = timezone.localtime(value)
        return super(DateTimeTzAwareField, self).to_native(value) """

class ApplyJobSerializer(serializers.ModelSerializer):

    """ updated_at = DateTimeTzAwareField(format="%d-%m-%Y  %H:%M")
    applydate = DateTimeTzAwareField(format="%d-%b-%Y  %H:%M")
 """
    def to_representation(self, instance):
        rep = super(ApplyJobSerializer, self).to_representation(instance)
        rep['job'] = instance.job.id
        rep['student'] = instance.student.id
        return rep

    class Meta:
        model = ApplyJob
        fields = ('id','job','student','body','resume','applydate','status','updated_at')
