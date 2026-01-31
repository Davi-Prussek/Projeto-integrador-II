from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(Consulta)
admin.site.register(Receita)
admin.site.register(Medicamento)
admin.site.register(ReceitaMedicamento)