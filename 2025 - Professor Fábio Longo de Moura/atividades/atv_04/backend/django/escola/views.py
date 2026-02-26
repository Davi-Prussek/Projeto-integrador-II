from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = alunoSerializer
class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = disciplinaSerializer
class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = professorSerializer
class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = turmaSerializer
class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = matriculaSerializer
class FrequenciaViewSet(ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = frequenciaSerializer