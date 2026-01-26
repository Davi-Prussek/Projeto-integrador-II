from django.contrib import admin
from .models import *

admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Matricula)
admin.site.register(Frequencia)