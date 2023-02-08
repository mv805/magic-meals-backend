from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'display_name', 'email', 'password']
    # id = serializers.IntegerField()
    # display_name = serializers.CharField(max_length=255)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=255)
