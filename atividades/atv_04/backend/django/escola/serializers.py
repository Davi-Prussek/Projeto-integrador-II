from rest_framework.serializers import ModelSerializer
from .models import *

class cursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class alunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"

class disciplinaSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class professorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
    
class turmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class matriculaSerializer(ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class frequenciaSerializer(ModelSerializer):
    class Meta:
        model = Frequencia
        fields = '__all__'