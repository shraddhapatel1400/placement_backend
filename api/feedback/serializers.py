from rest_framework import serializers
from .models import Feedback,Technology

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Feedback
        fields = ('id','name','email','subject','message','created_at')


class TechnologySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Technology
        image = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
        fields = ('id','name','description','image')
