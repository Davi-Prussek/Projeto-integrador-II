from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import * 
from .serializers import *

class PropriedadeViewSet(ModelViewSet):
    queryset = propriedade.objects.all()
    serializer_class = propriedadeSerializer

class CulturaViewSet(ModelViewSet):
    queryset = cultura.objects.all()
    serializer_class = culturaSerializer

class PlantioViewSet(ModelViewSet):
    queryset = plantio.objects.all()
    serializer_class = plantioSerializer

class ColheitaViewSet(ModelViewSet):
    queryset = colheita.objects.all()
    serializer_class = colheitaSerializer

class InsumoViewSet(ModelViewSet):
    queryset = insumo.objects.all()
    serializer_class = insumoSerializer

class Uso_InsumoViewSet(ModelViewSet):
    queryset = usoInsumo.objects.all()
    serializer_class = uso_insumoSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioViewSet

