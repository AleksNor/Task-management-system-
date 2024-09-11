from django.db import models
from django.utils import timezone


class Project(models.Model):
    """
    Model describing the project.

    Attributes:
        id (AutoField): Unique identifier for the project.
        name (CharField): Project name.
        description (TextField): Project description (optional).
        created_at (DateTimeField): Date and time of project creation,
            set automatically when the project is created.
        updated_at (DateTimeField): Date and time of the last project update,
            set automatically when the project is changed.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the project name as a string representation."""
        return self.name


class Task(models.Model):
    """
    A model representing the task associated with the project.

    Attributes:
        id (AutoField): Unique identifier for the task.
        title (CharField): Task name.
        description (TextField): Task description (optional).
        due_date (DateField): Date of task completion.
        status (CharField): Current status of the task,
            e.g. 'to do', 'in-progress', 'completed', 'overdue'.
        project_id (ForeignKey): Relationship to the project to which
            the task relates.
        created_at (DateTimeField): Date and time of task creation,
            set automatically when the task is created.
        updated_at (DateTimeField): Date and time of the last task update,
            set automatically when the task is changed.
    """

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='todo')
    project_id = models.ForeignKey(Project, related_name='tasks',
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def check_status(self):
        """
        Checks the task status and updates it if the task is overdue.

        If the due date of the task is less than the current date and the status
        is not equal to 'completed', the status is updated to 'overdue'.
        """
        if self.due_date < timezone.now().date() and self.status != 'completed':
            self.status = 'overdue'
        self.save()



