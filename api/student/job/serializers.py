from rest_framework import serializers

from .models import Summary

class JobSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(JobSerializer, self).to_representation(instance)
        rep['student'] = instance.student.id
        return rep

    class Meta:
        model = Summary
        fields = ('id','student','position','experience','objective')
