from django.test import TestCase
from django.test.client import Client
from profiles_api.models import UserProfile
from django.urls import reverse,resolve
from rest_framework import status
from profiles_api.serializers import UserProfileSerializer
import pytest
import json
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserProfile.objects.create_user(
            email='gmail@gmail.com', password='password', name='dee')
        self.user_payload={
            'email':'gmail2@gmail.com',
            'name':'dee256',
            'password':'Adddddd'
        }
    def test_get_user_profiles(self):
        res = self.client.get('/api/profile/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        user_profiles=UserProfile.objects.all()
        serializer=UserProfileSerializer(user_profiles,many=True)
        self.assertEqual(res.data,serializer.data)

    def test_get_a_user_profile(self):
        res=self.client.get('/api/profile/1/')
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        user_profile=UserProfile.objects.get(pk=1)
        serializer=UserProfileSerializer(user_profile)
        self.assertEqual(res.data,serializer.data)
    
    def test_create_profile(self):
        res=self.client.post('/api/profile/',
        data=json.dumps(self.user_payload),content_type='application/json')

        self.assertEqual(res.status_code,status.HTTP_200_OK)
        
        
