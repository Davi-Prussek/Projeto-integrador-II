from rest_framework.serializers import ModelSerializer
from .models import *

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class FuncionarioServicoSerializer(ModelSerializer):
    class Meta: 
        model = FuncionarioServico
        fields = '__all__'

class HospedeSerializer(ModelSerializer):
    class Meta: 
        model = Hospede
        fields = '__all__'

class HospedeReservaSerializer(ModelSerializer):
    class Meta: 
        model = HospedeReserva
        fields = '__all__'

class PagamentoSerializer(ModelSerializer):
    class Meta: 
        model = Pagamento
        fields = '__all__'

class QuartoSerializer(ModelSerializer):
    class Meta: 
        model = Quarto
        fields = '__all__'

class ReservaSerializer(ModelSerializer):
    class Meta: 
        model = Reserva
        fields = '__all__'

class ReservaPagamentoSerializer(ModelSerializer):
    class Meta: 
        model = ReservaPagamento
        fields = '__all__'

class ReservaServicoSerializer(ModelSerializer):
    class Meta: 
        model = ReservaServico
        fields = '__all__'

class ServicoSerializer(ModelSerializer):
    class Meta: 
        model = Servico
        fields = '__all__'