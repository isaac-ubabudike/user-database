from django.shortcuts import render

from django.contrib.auth.models import User # imports user from django backend 
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer  # Imports the class we created in serializers
from rest_framework.permissions import IsAuthenticated, AllowAny  #AllowANyone
from .models import Note


# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # cannot access this route unless u pass a valid JWT token

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=User) #makes it so that your are only viewing notes read by you and not by someones else.
    
    def perform_create(self, serializer): # we want custom config to overide the create method
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # cannot access this route unless u pass a valid JWT token

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=User) #makes it so that you can only delete yout information

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()  # Ensures no duplicates of existing objects
    serializer_class = UserSerializer  # Specifies the needed information to make a new user which is 'id', 'username', 'password'
    permission_classes = [AllowAny]  # Allows anyone even without authentication, inorder to create a new user