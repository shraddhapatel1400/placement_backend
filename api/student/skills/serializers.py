from rest_framework import serializers

from .models import Skills

class SkillSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(SkillSerializer, self).to_representation(instance)
        rep['student'] = instance.student.id
        return rep

    class Meta:
        model = Skills
        fields = ('id','student','skill','level')
