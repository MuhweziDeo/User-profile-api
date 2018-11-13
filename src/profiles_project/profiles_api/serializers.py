from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """ serializers a name field for testing our apiview """
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.Serializer):
	""" Seriailzer for user Profile object"""

	class Meta:
		model=models.UserProfile
		fields=('id','email','name','password')
		extra_kwargs={'password':{'write_only':True}}
		# makes password field readonly

	def create(self,validated_data):
		"""create and return a user"""
		user=models.UserProfile(
			email=validated_data['email'],
			name=validated_data['name']
			)
		user.set_password(validated_data['password'])
		user.save()
		return user
