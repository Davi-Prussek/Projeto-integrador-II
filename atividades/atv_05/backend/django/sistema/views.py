from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FuncionarioServicoViewSet(ModelViewSet):
    queryset = FuncionarioServico.objects.all()
    serializer_class = FuncionarioServicoSerializer
    
class HospedeViewSet(ModelViewSet):
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer

class HospedeReservaViewSet(ModelViewSet):
    queryset = HospedeReserva.objects.all()
    serializer_class = HospedeReservaSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class QuartoViewSet(ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer

class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaPagamentoViewSet(ModelViewSet):
    queryset = ReservaPagamento.objects.all()
    serializer_class = ReservaPagamentoSerializer

class ReservaServicoViewSet(ModelViewSet):
    queryset = ReservaServico.objects.all()
    serializer_class = ReservaServicoSerializer

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer