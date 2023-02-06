from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    display_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
