from rest_framework import serializers

from .models import Project

class ProjectSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(ProjectSerializer, self).to_representation(instance)
        rep['student'] = instance.student.id
        return rep

    class Meta:
        model = Project
        fields = ('id','student','title','description','technology','database')
