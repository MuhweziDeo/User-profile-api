from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """ serializers a name field for testing our apiview """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.Serializer):
    """ Seriailzer for user Profile object"""
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = models.UserProfile
        # fields = ('id', 'email', 'name', 'password')
        # extra_kwargs = {'password': {'write_only': True}}

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

    def update(self, request, pk=None,*args, **kwargs):
        self.queryset = models.UserProfile.objects.all()
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        self.queryset = models.UserProfile.objects.all()
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
