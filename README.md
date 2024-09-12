![PythonAnywhere](https://img.shields.io/badge/python-%232F9FD7.svg?style=for-the-badge&logo=pythonanywhere&logoColor=151515)   ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
# Task Management System

## Описание

Это репозиторий для системы управления задачами, которая включает функциональность для управления проектами и задачами в рамках этих проектов. Система предоставляет REST API для выполнения следующих операций
* Управление проектами:
	+ Создание нового проекта.
	+ Просмотр списка всех проектов.
	+ Просмотр деталей конкретного проекта.
	+ Обновление информации о проекте.
	+ Удаление проекта.
* Управление задачами:
	+ Создание новой задачи в рамках проекта.
	+ Просмотр списка всех задач в рамках проекта.
	+ Просмотр деталей конкретной задачи.
	+ Обновление информации о задаче.
	+ Удаление задачи.


## Инструкция по установке и запуску

Чтобы установить и запустить систему, следуйте этим шагам:

* Установите виртуальное окружение
* Установите зависимости
'pip install -r requirements.txt'
* Перейдите в папку task_manager, создайте и выполните миграции
```
python manage.py makemigrations
python manage.py migrate
```
* Запуск тестов
`python manage.py test tasks`
* Запуск проекта
`python manage.py runserver`
### Доступные адреса
1. Swager документация доступна по url http://127.0.0.1:8000/api/schema/swagger/
2. Проекты по url http://127.0.0.1:8000/api/projects/, для входа в конкретный проект добавьте его id
3. Задачи по url http://127.0.0.1:8000/api/projects/id_projects/tasks/, для входа в конкретную задачу добавьте ее id (вместо id_projects также подставьте id проекта)
