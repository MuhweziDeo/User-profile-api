from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """ serializers a name field for testing our apiview """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Seriailzer for user Profile object"""
    """ 
   	if u dont inherit from ModelSerializer class then set this fields

   	id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=100, write_only=True) """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        # makes password field readonly

    def create(self, validated_data):
        """create and return a user"""
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    """ 
    only define this methods in u dont in herit from ModelSerializer class

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

         """
    