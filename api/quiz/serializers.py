from rest_framework import serializers

from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        rep = super(QuizSerializer, self).to_representation(instance)
        rep['company'] = instance.company.id
        return rep

    class Meta:
        model = Quiz
        fields = ('id','company','question','option1','option2','option3','option4','answer')
