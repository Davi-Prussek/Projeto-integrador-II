from django.db import models

class propriedade(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=120)
    def __str__(self):
        return f'{self.nome} - {self.endereco}'

class cultura(models.Model):
    nome = models.CharField(max_length=50)
    duracao_dias = models.IntegerField()
    def __str__(self):
        return f'{self.nome} - {self.duracao_dias}'

class plantio(models.Model):
    propriedade = models.ForeignKey(propriedade, on_delete=models.PROTECT, related_name='plantios')
    cultura = models.ForeignKey(cultura, on_delete=models.PROTECT)
    def __str__(self):
        return f'{self.propriedade} - {self.cultura}'

class colheita(models.Model):
    data_inicio = models.DateField()
    data_final = models.DateField()
    plantio = models.ForeignKey(plantio, on_delete=models.PROTECT, related_name='colheitas')
    def __str__(self):
        return f'{self.data_inicio} - {self.data_final} - {self.plantio}'

class insumo(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.nome} - {self.unidade}'

class usoInsumo(models.Model):
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    plantio = models.ForeignKey(plantio, on_delete=models.PROTECT, related_name='Uso_de_Insumos')
    insumo = models.ForeignKey(insumo, on_delete=models.PROTECT, related_name='Uso_de_insumos')
    def __str__(self):
        return f'{self.quantidade} - {self.data} - {self.plantio} - {self.insumo}'

class funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    CPF = models.CharField(max_length=25)
    RG = models.CharField(max_length=20)
    propriedade = models.ForeignKey(propriedade, on_delete=models.PROTECT, related_name='Funcionarios')
    def __str__(self):
        return f'{self.nome} - {self.cargo}'