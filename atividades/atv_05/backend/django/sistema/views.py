from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]

class FuncionarioServicoViewSet(ModelViewSet):
    queryset = FuncionarioServico.objects.all()
    serializer_class = FuncionarioServicoSerializer
    permission_classes = [IsAuthenticated]

class HospedeViewSet(ModelViewSet):
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer
    permission_classes = [IsAuthenticated]

class HospedeReservaViewSet(ModelViewSet):
    queryset = HospedeReserva.objects.all()
    serializer_class = HospedeReservaSerializer
    permission_classes = [IsAuthenticated]

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = [IsAuthenticated]

class QuartoViewSet(ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer

class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

class ReservaPagamentoViewSet(ModelViewSet):
    queryset = ReservaPagamento.objects.all()
    serializer_class = ReservaPagamentoSerializer
    permission_classes = [IsAuthenticated]

class ReservaServicoViewSet(ModelViewSet):
    queryset = ReservaServico.objects.all()
    serializer_class = ReservaServicoSerializer
    permission_classes = [IsAuthenticated]

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = [IsAuthenticated]
