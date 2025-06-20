from django.shortcuts import render, get_object_or_404

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Confeccion
from .serializer import UserSerializer, ConfeccionSerializer



@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#HTTP PARA CONFECCIONES#

@api_view(['GET'])
def get_confeccion(request):
    confecciones = Confeccion.objects.all()
    serializer = ConfeccionSerializer(confecciones, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_confeccion(request):
    serializer = ConfeccionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH', 'DELETE'])
def update_delete_confeccion(request, id):
    confeccion = get_object_or_404(Confeccion, id=id)
    
    if 'code' in request.data and request.data['code'] != confeccion.code:
        pass
    
    if request.method == 'PUT':
        serializer = ConfeccionSerializer(confeccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ConfeccionSerializer(confeccion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        confeccion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
