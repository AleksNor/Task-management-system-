from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'projects/(?P<project_id>[^/.]+)/tasks', TaskViewSet,
                basename='project-tasks')

urlpatterns = [
    path('', include(router.urls)),
]
