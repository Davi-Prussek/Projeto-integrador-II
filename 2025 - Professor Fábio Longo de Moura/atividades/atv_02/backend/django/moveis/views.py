from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class ClienteViewSet(ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer

class PedidoViewSet(ModelViewSet):
    queryset = pedido.objects.all()
    serializer_class = pedidoSerializer

class MateriaPrimaViewSet(ModelViewSet):
    queryset = materiaPrima.objects.all()
    serializer_class = materiaPrimaSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = produto.objects.all()
    serializer_class = produtoSerializer

class ItemPedidoViewSet(ModelViewSet):
    queryset = itemPedido.objects.all()
    serializer_class = itemPedidoSerializer

class OrdemProducaoViewSet(ModelViewSet):
    queryset = ordemProducao.objects.all()
    serializer_class = ordemProducaoSerializer
class FuncionarioViewSet(ModelViewSet):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer