from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'display_name', 'email', 'password']

class UserDisplayNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['display_name']    
    #! example of a validate override
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passwords no matchy')
    #     return data
    #! standard fields for non model serializer    
    # id = serializers.IntegerField()
    # display_name = serializers.CharField(max_length=255)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=255)
