from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer, UserProfileSerializer
from . import models
from . import permissions
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.


class HeloApViews(APIView):
    """ Test API View"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APi view functions """
        api_view = [
            'uses HTPP methods as a function(get,post,put,patch,delete)',
            'its simillar to a traditional django view',
            'Gives u the most control over logic',
            'its mapped manually to urls'
        ]

        return Response({'message': 'View', 'api_view': api_view})

    def post(self, request):
        """ create a hello message with our name"""
        serializer = HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """  handles updating an object"""

        return Response({'method': "put"})

    def patch(self, request, pk=None):
        """  handles updating an fields provided in a request"""

        return Response({'method': "patch"})

    def delete(self, request, pk=None):
        """  handles updating an object"""

        return Response({'method': "delete"})


class HeloViewSet(viewsets.ViewSet):
    """ Test API viewsets"""
    serializer_clash = HelloSerializer

    def list(self, request):
        """ Return simple message"""

        api_viewset = [
            "uses actions(list,create,retrieve,update,partial_update)",
            "automatically maps to URLS using Router",
            "provides more functionality with less code"

        ]

        return Response({'message': 'Hello HeloViewSet', 'api_viewset': api_viewset})

    def create(self, request):
        """ create a new hello message"""
        serializer = HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)

            return Response({'message': message})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handles getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handles updating an object by its ID"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handles updatinf part an object by its ID"""
        return Response({'http_method': 'PATCh'})

    def destroy(self, request, pk=None):
        """handles removin an object by its ID"""
        return Response({'http_method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handles creating updating and deleting user profiles"""
    queryset = models.UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """ logins in user and returns auth token """
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """ use the obtainauthtoken apiview to validate and create a token"""
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ handles creating reading and updatinf profile feed items"""

    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedSerializer
    queryset=models.ProfileFeedItem.objects.all() 

    def perform_create(self,serializer):
        """ sets userprofile to logged in user"""
        serializer.save(user_profile=self.request.user)


