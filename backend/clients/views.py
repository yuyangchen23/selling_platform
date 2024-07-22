from django.shortcuts import render
from .serializer import ClientSerializer
from rest_framework import viewsets
from .models import Client

# Create your views here.
class ClientViewSets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    