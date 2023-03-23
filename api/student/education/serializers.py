from rest_framework import serializers

from .models import Education

class EducationSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(EducationSerializer, self).to_representation(instance)
        rep['student'] = instance.student.id
        return rep

    class Meta:
        model = Education
        fields = ('id','student','course','board','yearofpassing','ogpa')
