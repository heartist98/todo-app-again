from django.http import HttpResponse  # Keep this for home view
from rest_framework import viewsets, filters  # Add filters for search and filtering
from django_filters.rest_framework import DjangoFilterBackend  # Add this for filtering
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']  # Allow searching by title
    filterset_fields = ['completed']  # Filter tasks by 'completed' status

def home_view(request):
    return HttpResponse("""
        <h1>Todo API Working!</h1>
        <p><a href='/api/tasks/'>API Endpoint</a></p>
        <p><a href='/admin/'>Admin Panel</a></p>
    """)
