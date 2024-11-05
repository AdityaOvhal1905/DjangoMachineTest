# myapp/urls.py

from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectListCreateView, ProjectDetailView
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),  # Removed space after 'clients'
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('clients/<int:client_id>/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/', generics.ListAPIView.as_view(queryset=Project.objects.all(), serializer_class=ProjectSerializer), name='project-list'),
]