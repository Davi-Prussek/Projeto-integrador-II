from django.contrib import admin
from .models import *

admin.site.register(Funcionario)
admin.site.register(FuncionarioServico)
admin.site.register(Hospede)
admin.site.register(HospedeReserva)
admin.site.register(Pagamento)
admin.site.register(Quarto)
admin.site.register(Reserva)
admin.site.register(ReservaPagamento)
admin.site.register(ReservaServico)
admin.site.register(Servico)