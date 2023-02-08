from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer


def index(request):
    return Response("Hello, world. You're at the meals app index.")

# return a list of all user groups


@api_view()
def all_user_group_list(request):
    return Response('ok')


@api_view()
def all_users_list(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_detail(request, id):
    if request.method == 'GET':
        user = get_object_or_404(User, pk=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('saved user')
