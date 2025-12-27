from rest_framework.serializers import ModelSerializer
from .models import Estado, Cidade, Aluno

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class alunosSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'