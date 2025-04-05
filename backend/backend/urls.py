# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos.views import TaskViewSet, home_view  # Updated imports

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # Uses ViewSet

urlpatterns = [
    path('', home_view),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]