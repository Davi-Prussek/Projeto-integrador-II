"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import *

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'disciplina', DisciplinaViewSet)
router.register(r'professor', ProfessorViewSet)
router.register(r'turma', TurmaViewSet)
router.register(r'matricula', MatriculaViewSet)
router.register(r'frequencia', FrequenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
