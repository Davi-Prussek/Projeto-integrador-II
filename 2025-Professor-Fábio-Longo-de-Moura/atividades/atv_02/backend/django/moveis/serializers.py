from rest_framework.serializers import ModelSerializer
from .models import *

class clienteSerializer(ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class pedidoSerializer(ModelSerializer):
    class Meta:
        model = pedido
        fields = '__all__'

class materiaPrimaSerializer(ModelSerializer):
    class Meta:
        model = materiaPrima
        fields = '__all__'

class produtoSerializer(ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'

class itemPedidoSerializer(ModelSerializer):
    class Meta:
        model = itemPedido
        fields = '__all__'

class ordemProducaoSerializer(ModelSerializer):
    class Meta:
        model = ordemProducao
        fields = '__all__'

class funcionarioSerializer(ModelSerializer):
    class Meta:
        model = funcionario
        fields = '__all__'