from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Project, Task
import datetime


class ProjectAPITests(APITestCase):
    """
    Тесты для управления проектами через API.
    """

    def setUp(self):
        """
        Создаем тестовый проект для дальнейших тестов.
        """
        self.project_data = {
            "name": "Test Project",
            "description": "Project description"
        }
        self.project = Project.objects.create(**self.project_data)

    def test_create_project(self):
        """
        Тест на создание нового проекта.
        """
        response = self.client.post(reverse('project-list'), self.project_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)

    def test_get_projects(self):
        """
        Тест на получение списка всех проектов.
        """
        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.count(), 1)

    def test_get_project_details(self):
        """
        Тест на получение деталей конкретного проекта.
        """
        response = self.client.get(reverse('project-detail',
                                           kwargs={'pk': self.project.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.project.name)

    def test_update_project(self):
        """
        Тест на обновление информации о проекте.
        """
        updated_data = {
            "name": "Updated Project",
            "description": "Updated description"
        }
        response = self.client.put(reverse(
                        'project-detail',
                        kwargs={'pk': self.project.id}),
                        updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Project")

    def test_delete_project(self):
        """
        Тест на удаление проекта.
        """
        response = self.client.delete(reverse('project-detail',
                                              kwargs={'pk': self.project.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 0)


class TaskAPITests(APITestCase):
    """
    Тесты для управления задачами через API.
    """

    def setUp(self):
        """
        Создаем тестовый проект и задачу для дальнейших тестов.
        """
        self.project = Project.objects.create(name="Test Project",
                                              description="Project description")
        self.task_data = {
            "title": "Test Task",
            "description": "Task description",
            "due_date": str(datetime.date.today()+datetime.timedelta(days=1)),
            "status": "todo",
            "project_id": self.project
        }
        self.task = Task.objects.create(**self.task_data)

    def test_create_task(self):
        """
        Тест на создание новой задачи в проекте.
        """
        response = self.client.post(
            reverse(
                'project-tasks-list',
                kwargs={"project_id": self.project.id}),
            {
                "title": "Test Task",
                "description": "Task description",
                "due_date": str(
                    datetime.date.today() + datetime.timedelta(days=1)),
                "status": "todo",
                "project_id": self.project.id
            }
            )

        print(self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_tasks(self):
        """
        Тест на получение списка всех задач в проекте.
        """
        response = self.client.get(reverse(
            'project-tasks-list',
            kwargs={"project_id": self.project.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)

    def test_get_task_details(self):
        """
        Тест на получение деталей конкретной задачи.
        """
        response = self.client.get(
            reverse(
                'project-tasks-detail',
                kwargs={"project_id": self.project.id, 'pk': self.task.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        """
        Тест на обновление информации о задаче.
        """
        updated_data = {
            "title": "Updated Task",
            "description": "Updated description",
            "due_date": str(datetime.date.today()+datetime.timedelta(days=2)),
            "status": "in-progress",
            "project_id": self.project.id
        }
        response = self.client.put(
            reverse('project-tasks-detail',
                    kwargs={"project_id": self.project.id, 'pk': self.task.id}),
            updated_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Task")

    def test_delete_task(self):
        """
        Тест на удаление задачи.
        """
        response = self.client.delete(
            reverse('project-tasks-detail',
                    kwargs={"project_id": self.project.id, 'pk': self.task.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_status_due_date_check(self):
        """
        Тест на проверку обновления статуса задачи в зависимости от срока
        выполнения.
        """
        overdue_task_data = {
            "title": "Overdue Task",
            "description": "Overdue description",
            "due_date": str(datetime.date.today() - datetime.timedelta(days=1)),
            "status": "todo",
            "project_id": self.project.id
        }
        response = self.client.put(
            reverse('project-tasks-detail',
                    kwargs={"project_id": self.project.id, 'pk': self.task.id}),
            overdue_task_data)
        self.assertEqual(response.data['status'], "overdue")
