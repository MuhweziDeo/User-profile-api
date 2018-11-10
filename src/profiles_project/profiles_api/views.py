from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
# Create your views here.
class HeloApViews(APIView):
    """ Test API View"""
    serializer_class=HelloSerializer()
    def get(self,request,format=None):
        """ Returns a list of APi view functions """
        api_view=[
            'uses HTPP methods as a function(get,post,put,patch,delete)',
            'its simillar to a traditional django view',
            'Gives u the most control over logic',
            'its mapped manually to urls'
        ]

        return Response({'message':'View','api_view':api_view})

    def post(self,request):
        """ create a hello message with our name"""
        serializer=HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
