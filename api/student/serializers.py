from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes,permission_classes
from django.conf import settings
from .models import Student
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from django.contrib.auth.password_validation import validate_password

class StudentSerializer(serializers.HyperlinkedModelSerializer):

    def validate_password(self, data):
        validators.validate_password(password=data, user=Student)
        return data

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        
        enc_password = make_password(password)
        
        instance.password = enc_password
        instance.save()
        return instance
        

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                enc_password = make_password(value)
                instance.password = enc_password
            else:
                setattr(instance,attr,value)
        instance.save()
        return instance

    def to_representation(self, instance):
        rep = super(StudentSerializer, self).to_representation(instance)
        rep['created_at'] = instance.created_at.strftime("%d-%b-%Y")
        return rep

    class Meta:
        model = Student
        image = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
        pdf = serializers.FileField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
        fields = ('id','firstname','lastname','email','password','image','address','phone','pdf','status','created_at')
