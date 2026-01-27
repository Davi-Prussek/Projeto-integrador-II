from django.db import models

class Curso(models.Model):
    nome_curso = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_curso

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    numero_matricula = models.IntegerField(unique=True)
    data_nascimento = models.DateField()
    RG = models.CharField(max_length=25)
    CPF = models.CharField(max_length=30)
    nome_mae = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100)
    data_matricula = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} - {self.numero_matricula} - {self.data_nascimento} - {self.RG} - {self.CPF} - {self.nome_mae} - {self.nome_pai} - {self.data_matricula} - {self.curso}'

class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    carga_horaria = models.IntegerField()
    def __str__(self):
        return f'{self.nome} - {self.carga_horaria}'

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_admissao = models.DateField()
    RG = models.CharField(max_length=25)
    CPF = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.nome} - {self.data_nascimento} - {self.data_admissao} - {self.RG} - {self.CPF}'

class Turma(models.Model):
    nome = models.CharField(max_length=15)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ano = models.IntegerField()
    def __str__(self):
        return f'{self.nome} - {self.disciplina} - {self.professor} - {self.ano}'

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateField()
    def __str__(self):
        return f'{self.aluno} - {self.curso} - {self.data_matricula}'

class Frequencia(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField()
    class Meta:
        unique_together = (('aluno', 'turma', 'disciplina', 'data'),)
    def __str__(self):
        return f'{self.turma} - {self.disciplina} - {self.aluno} - {self.data} - {self.presente}'