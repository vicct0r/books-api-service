from django.shortcuts import render
from .serializers import LivroSerializers
from .models import Livro
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import generics


class LivrosAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers


class LivroAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers