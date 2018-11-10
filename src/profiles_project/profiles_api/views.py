from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class HeloApViews(APIView):
    """ Test API View"""
    def get(self,request,format=None):
        """ Returns a list of APi view functions """
        api_view=[
            'uses HTPP methods as a function(get,post,put,patch,delete)',
            'its simillar to a traditional django view',
            'Gives u the most control over logic',
            'its mapped manually to urls'
        ]

        return Response({'message':'View','api_view':api_view})