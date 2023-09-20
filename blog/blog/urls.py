"""appYoutube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('sair/', views.sair, name='sair'),
    path('tasks/', views.tasks, name='tasks'),
    path('create/tasks', views.create_tasks, name='create_tasks'),
    path('create/<int:task_id>/', views.task_detalhes, name='task_detalhes'),
    path('create/<int:task_id>/completed', views.completed_tarefa, name='completed_tarefa'),
    path('deleted_tarefa/<int:task_id>/', views.deleted_tarefa, name='deleted_tarefa'),
    path('exibir_tarefas_completadas', views.exibir_tarefas_completadas, name='exibir_tarefas_completadas'),
]