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

class Paciente(models.Model):
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
    def __str__(self):
        return f'{self.nome} - {self.sexo} - {self.data_nascimento} - {self.tipo_sanguineo} - {self.alergias}'

class Especialidade(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField(max_length=500)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.nome} - {self.descricao} - {self.ativo}'

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    colaterais = models.TextField(max_length=500)
    tipo_de_uso = models.CharField(max_length=20)
    tarja = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.nome} - {self.colaterais} - {self.tipo_de_uso} - {self.tarja}'

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    RG = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=25)
    email = models.CharField(max_length=320)
    endereco = models.CharField(max_length=100)
    cargo = models.CharField(max_length=40)
    ativo_atualmente = models.BooleanField(default=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT, related_name='medicos')
    def __str__(self):
        return f'{self.nome} - {self.email} - {self.cargo} - {self.ativo_atualmente} - {self.especialidade}'

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='consultas')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='consultas')
    def __str__(self):
        return f'{self.paciente} - {self.medico}'

class Receita(models.Model):
    forma_de_usar = models.TextField(max_length=500)
    consulta = models.ForeignKey(Consulta, on_delete=models.PROTECT, related_name='receitas')
    data_emissao = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.forma_de_usar} - {self.consulta} - {self.data_emissao}'

class ReceitaMedicamento(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.PROTECT)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    dosagem = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.receita} - {self.medicamento} - {self.dosagem}'