from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from .services import *

class ProfileView(APIView):
    def get(self,request):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response('404', status=status.HTTP_404_NOT_FOUND)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data,status=status.HTTP_200_OK)


class RegisterView(APIView):

    def post(self,request,):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Successfuly register!',status=201)
        return Response(serializer.errors,status=400)

class LoginView(APIView):

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializers.data.get('username')
            password = serializers.data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)

            return Response('welcome')
        return Response(serializers.errors)

    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('OK', status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        profile = Profile.objects.get(user=request.user)
        profile.delete()
        return Response('DELETED', status=200)




