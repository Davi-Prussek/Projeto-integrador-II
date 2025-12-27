from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Estado, Cidade, Aluno
from .serializers import EstadoSerializer, CidadeSerializer, alunosSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = alunosSerializer