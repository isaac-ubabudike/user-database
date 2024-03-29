from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# helps to Serializer validate the User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}} 
        # '{'write_only': True}'We want to accept password when creating a new user, 
        # but we dont want to return the password when we are giving information about the user
        # When we set the write only to true it means no one can read what the password is which is intentional


    def create(self, validate_data): # we taking in 'self' and 'validate_data'
        user = User.objects.create_user(**validate_data)
        return user
    
    #all this is doing is implementing a method that will be called when we want to create a new version of this user.
    # it first goes through the serilizer which ensures the user has valid information specified especially 'id', 'username', 'password'
    # and tehn you can create a new

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notefield = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwrags = {'author': {'read_only': True}} # Set by the backend, not the author