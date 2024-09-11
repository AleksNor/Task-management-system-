from rest_framework import viewsets
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project instances.

    This viewset provides standard actions such as:
    - GET: Get a list of projects
    - POST: Create a new project
    - GET: Get a single project by ID
    - PUT: Update an existing project
    - PATCH: Partial update of an existing task
    - DELETE: Delete an existing project
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing task instances associated with a project.

    This viewset provides standard actions such as:
    - GET: Get a list of tasks, optionally filtered by status and due date.
    - POST: Create a new task associated with a project.
    - GET: Get a single task by ID.
    - PUT: Update an existing task.
    - PATCH: Partial update of an existing task
    - DELETE: Delete an existing task.

    Filtering can be applied using the following query parameters:
    - status: Filter tasks by status.
    - due_date: Filter tasks by their due date.

    Note: The tasks returned will be restricted to the specified project ID.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = [
        'status',
        'due_date'
    ]

    def get_queryset(self):
        """
        Optionally restricts the returned tasks to a given project
        based on the project_id in the URL.

        Returns:
            QuerySet: A queryset of tasks filtered by the project ID,
            and optionally further filtered by status if provided
            in the query parameters.
        """
        project_id = self.kwargs.get('project_id')
        queryset = Task.objects.filter(project_id=project_id)
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
