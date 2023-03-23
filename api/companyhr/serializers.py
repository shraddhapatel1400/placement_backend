from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes,permission_classes
from django.conf import settings
from .models import CompanyHr
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from django.contrib.auth.password_validation import validate_password

class CompanyHrSerializer(serializers.HyperlinkedModelSerializer):

    def validate_password(self, data):
        validators.validate_password(password=data, user=CompanyHr)
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


    class Meta:
        model = CompanyHr
        image = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
        fields = ('id','fullname','email','password','companyname','logo','location','phone','status','criteria','created_at')
