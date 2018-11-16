from django.test import TestCase
from django.test.client import Client
from profiles_api.models import UserProfile
from django.urls import reverse,resolve
from rest_framework import status
from profiles_api.serializers import UserProfileSerializer
import pytest

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserProfile.objects.create_user(
            email='gmail@gmail.com', password='password', name='dee')

    def test_get_user_profiles(self):
        res = self.client.get('/api/profile/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        user_profiles=UserProfile.objects.all()
        serializer=UserProfileSerializer(user_profiles,many=True)
        self.assertEqual(res.data,serializer.data)
        
