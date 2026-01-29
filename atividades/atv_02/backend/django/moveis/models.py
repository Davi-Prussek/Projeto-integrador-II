from django.db import models

class cliente(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=30)
    RG = models.CharField(max_length=15)
    CPF = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.nome}'

class pedido(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.PROTECT,related_name='Pedidos')
    data = models.DateField()
    status = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.cliente} - {self.data} - {self.status}'

class materiaPrima(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{self.nome} - {self.preco}'

class produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    materia_prima = models.ManyToManyField(materiaPrima)
    def __str__(self):
        return f'{self.nome} - {self.preco} - {self.materia_prima}'

class itemPedido(models.Model):
    pedido = models.ForeignKey(pedido, on_delete=models.PROTECT, related_name='itens')
    produto = models.ForeignKey(produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.pedido} - {self.produto} - {self.quantidade}'

class ordemProducao(models.Model):
    produto = models.ForeignKey(produto,on_delete=models.PROTECT,related_name='Ordem_de_producoes')
    quantidade = models.PositiveIntegerField()
    data_inicio = models.DateField()
    data_final = models.DateField()
    conclusao = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.produto} - {self.quantidade} - {self.data_inicio} - {self.data_final} - {self.conclusao}'

class funcionario(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=30)
    RG = models.CharField(max_length=15)
    CPF = models.CharField(max_length=20)
    cargo = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.nome} - {self.cargo}'