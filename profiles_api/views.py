from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """ test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request, format=None):
        """ Returns the List ApiView Feature"""
        an_apiview = [
            'user HTTp method as function(get, post, patch,put,delete)',
            'Is similar to a traditional django View',
            'Gives you the most control over you application logic',
            'Is mappped manually to URls'
        ]

        return Response({'message':'Hello!' ,'an_apiview':an_apiview})

    def post(self,request):
        """ create the hello massage with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """ Handle Updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """ Handle a partial update of an object """
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """ Delete the request of an object """
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """
    serializer_class =serializers.HelloSerializer

    def list(self,request):
        """ return a hello message """
        a_viewset=[
            'Uses action(list, create, retrive, update, portial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!' ,'a_viewset':a_viewset})

    def create(self,request):
        """ create a new hello message """
        serializer =self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self,requst,pk=None):
        """ Handle getting an object by its Id """
        return Response({'http_method':'GET'})

    def update(self,requst,pk=None):
        """ Handle update an object """
        return Response({'http_method':'PUT'})
    
    def partial_update(self,requst,pk=None):
        """ Handle updating part an object """
        return Response({'http_method':'PATCH'})
    
    def destroy(self,requst,pk=None):
        """ Handle remove an object """
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating  profile """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)