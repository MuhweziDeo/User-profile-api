from django.test import TestCase
from profiles_api.models import UserProfile
import pytest

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user=UserProfile.objects.create_user(email="aggrey300@gmail.com",password="Adeo256.",name='dee')


    def test_user_created(self):
        self.assertEqual("aggrey300@gmail.com",str(self.user))

    def test_create_user_validation(self):
        with pytest.raises(ValueError):
        	invalid_user=UserProfile.objects.create_user(email="",password="Adeo256.",name='dee')

