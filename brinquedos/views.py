from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Brinquedo
from .serializers import BrinquedoSerializer

@api_view(['GET', 'POST'])
def brinquedo_list(request):
    if request.method == 'GET':
        brinquedos = Brinquedo.objects.all()
        serializer = BrinquedoSerializer(brinquedos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BrinquedoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def brinquedo_detail(request, pk):
    brinquedo = get_object_or_404(Brinquedo, pk=pk)

    if request.method == 'GET':
        serializer = BrinquedoSerializer(brinquedo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BrinquedoSerializer(brinquedo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        brinquedo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
