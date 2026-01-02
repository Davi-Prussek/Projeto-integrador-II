"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from sistema.views import *

router = DefaultRouter()
router.register(r'Funcionario', FuncionarioViewSet)
router.register(r'Funcionario_Servico', FuncionarioServicoViewSet)
router.register(r'Hospede', HospedeViewSet)
router.register(r'Hospede_Reserva', HospedeReservaViewSet)
router.register(r'Pagamento', PagamentoViewSet)
router.register(r'Quarto', QuartoViewSet)
router.register(r'Reserva', ReservaViewSet)
router.register(r'Reserva_Pagamento', ReservaPagamentoViewSet)
router.register(r'Reserva_Servico', ReservaServicoViewSet)
router.register(r'Servico', ServicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
