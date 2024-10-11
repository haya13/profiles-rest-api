from tkinter.font import names

from django.core.serializers import serialize
from django.shortcuts import render
from pyexpat import features
from pyexpat.errors import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import  viewsets

class HelloAPIView(APIView):
    """an APIView that says hello"""

    serializer_class = serializers.HelloSerializer


    #HTTP Methods
    def get(self,request):
        """handles GET Methods to this APIView"""
        features = [                       #Read,Create,Update,delete
            "Uses HTTP methods as functions (Get, Post, Patch, Delete)",
            "Gives you control over the application logic",
            "Mapped manually by URLs"

        ]
        return Response({
            "message":"Hello",
            "feture":features
        })
    def post(self, request):
        """Return a Hello message to the subscriber"""
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message="Hello {}".format(name)
            return Response({"message:":message})
        return  Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk=None):  #Update  pk=primary ke
        """Updates an object partially"""
        return Response({"message":request.method})
    def put(self, request, pk=None):
        """Updates the object fully"""
        return Response({"message": request.method})
    def delete(self,request,pk=None):
        """deletes an object"""
        return Response({"message": request.method})


class HelloViewSet(viewsets.ViewSet):
    """Creates a Hello Viewset"""

    def list(self, request):
        """Returns a Hello message"""
        features = [
            "Uses Actions (list, create, retrieve, update, partial_update,destroy)",
            "provides functionality with less code",
            "Mapped Automatically using Routers "
        ]

        return  Response({
            "message":"Hello",
            "features":features
        }  )
    def create(self,request):
        """create a new hello Message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({"message:": message})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request):
        """handles getting an object by its primary key"""
        return Response({"message": request.method})
    def update(self,request,pk=None):
        return Response({"message":request.method})
    def partial_update(self,request,pk=None):
        return Response({"message":request.method})
    def destroy(self,request,pk=None):
        return Response({"message":request.method})













