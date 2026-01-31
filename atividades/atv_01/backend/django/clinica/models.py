from django.db import models

# Create your models here.
""" 
    Relacionamentos:

    Cada médico pertence a uma especialidade.
    Um paciente pode realizar várias consultas com diferentes médicos.
    Cada consulta pode gerar uma ou mais receitas, que podem conter múltiplos medicamentos.

💡 Exemplo de entidades:

    Paciente
    Medico
    Especialidade
    Consulta
    Receita
    Medicamento
    Receita_Medicamento

    salvar:
    
    sintomas = models.TextField(max_length=500)
"""

class paciente(models.Model):
    nome = models.CharField(max_length=100)
    RG = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=20)
    telefone = models.CharField(max_length=25)
    email = models.CharField(max_length=320)
    endereco = models.CharField(max_length=100)
    tipo_sanguineo = models.CharField(max_length=5)
    alergias = models.TextField(blank=True)

class medico(models.Model):
    nome = models.CharField(max_length=100)
    RG = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=25)
    email = models.CharField(max_length=320)
    endereco = models.CharField(max_length=100)
    cargo = models.CharField(max_length=40)
    ativo_atualmente = models.BooleanField(default=True)
    especialidade = models.ForeignKey(especialidade, on_delete=models.PROTECT, related_name='medicos')

class especialidade(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField(max_length=500)
    ativo = models.BooleanField(default=True)