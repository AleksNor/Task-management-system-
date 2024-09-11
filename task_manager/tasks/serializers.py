from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    """Project model serializer.

    This class converts the Project model to JSON format and back again.
    """
    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """Task model serializer.

    This class converts the Task model to JSON format and back.
    It also handles task creation and updating with status checking.
    """
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        """Creating a new task.

        When creating a new task, checks if it is overdue.

        Args:
            validated_data (dict): New task whose status is being checked.

        Returns:
            Task: Created task.
        """
        task = Task(**validated_data)
        task.check_status()
        return task

    def update(self, instance, validated_data):
        """Updating an existing task.

        Updates the specified task and checks its status after the update.

        Args:
            instance (Task): Task instance to be updated.
            validated_data (dict): Validated data for task update.

        Returns:
            Task: Updated task.
        """
        instance = super().update(instance, validated_data)
        instance.check_status()
        return instance
