from django.http import Http404
from django.contrib.auth import authenticate


from .serializers import CustomUserSerializer, Blog
from .models import CustomUser, Blog

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


# List all the users in the database
class UserList(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        if users.__len__() < 1:
            response = {'message':'No users available'}
            return Response(response, status=status.HTTP_204_NO_CONTENT)

        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


# Get single user
class UserDetail(APIView):

    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({'message': 'No user found'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk , format=None):
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        user = CustomUser.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)