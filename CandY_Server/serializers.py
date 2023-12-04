from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import TbMember

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# RegisterSerializer - Sign Up 
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True, required =True)

    class Meta:
        model = TbMember
        fields = ('user_id','password','password2','device_check')
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password":"Password didn't match."})
        return data
    def create(self, validated_data):
        validated_data.pop('password2', None)
        return TbMember.objects.create(**validated_data)