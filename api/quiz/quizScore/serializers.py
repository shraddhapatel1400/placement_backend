from rest_framework import serializers

from .models import QuizScore

class QuizScoreSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(QuizScoreSerializer, self).to_representation(instance)
        rep['student'] = instance.student.id
        rep['quiz'] = instance.quiz.id
        return rep

    class Meta:
        model = QuizScore
        fields = ('id','quiz','student','answer','score')
