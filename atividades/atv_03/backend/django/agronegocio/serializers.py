from rest_framework.serializers import ModelSerializer
from .models import *

class propriedadeSerializer(ModelSerializer):
    class Meta: 
        model = propriedade
        fields = '__all__'

class culturaSerializer(ModelSerializer):
    class Meta: 
        model = cultura
        fields = '__all__'

class plantioSerializer(ModelSerializer):
    class Meta: 
        model = plantio
        fields = '__all__'

class colheitaSerializer(ModelSerializer):
    class Meta: 
        model = colheita
        fields = '__all__'

class insumoSerializer(ModelSerializer):
    class Meta: 
        model = insumo
        fields = '__all__'

class uso_insumoSerializer(ModelSerializer):
    class Meta: 
        model = usoInsumo
        fields = '__all__'

class funcionarioSerializer(ModelSerializer):
    class Meta: 
        model = funcionario
        fields = '__all__'
