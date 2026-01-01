from django.db import models
from django.utils.html import format_html

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'funcionario'

    def __str__(self):
        return format_html(
            '<strong>Funcionario</strong> <ul> <li>id: {}</li><li>nome: {}</li><li>cargo: {}</li><li>email: {}</li><li>telefone: {}</li></ul>',
            self.id_funcionario,
            self.nome,
            self.cargo,
            self.email,
            self.telefone
        )

class FuncionarioServico(models.Model):
    id_funcionario = models.OneToOneField(Funcionario, models.DO_NOTHING, db_column='id_funcionario', primary_key=True)
    id_servico = models.ForeignKey('Servico', models.DO_NOTHING, db_column='id_servico')

    class Meta:
        managed = False
        db_table = 'funcionario_servico'
        unique_together = (('id_funcionario', 'id_servico'),)

    def __str__(self):
        return format_html(
            '<strong>FuncionarioServico</strong> <ul><li>Funcionario: {}</li><li>Servico: {}</li></ul>',
            self.id_funcionario.nome,
            self.id_servico.id_servico
        )

class Hospede(models.Model):
    id_hospede = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'hospede'

    def __str__(self):
        return format_html(
            '<strong>Hospede</strong> <ul><li>id: {}</li><li>nome: {}</li><li>email: {}</li><li>telefone: {}</li></ul>',
            self.id_hospede,
            self.nome,
            self.email,
            self.telefone
        )

class HospedeReserva(models.Model):
    id_reserva = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='id_reserva', primary_key=True)
    id_hospede = models.ForeignKey(Hospede, models.DO_NOTHING, db_column='id_hospede')

    class Meta:
        managed = False
        db_table = 'hospede_reserva'
        unique_together = (('id_reserva', 'id_hospede'),)

    def __str__(self):
        return format_html(
            '<strong>HospedeReserva</strong> <ul><li>Reserva: {}</li><li>Hospede: {}</li></ul>',
            self.id_reserva.id_reserva,
            self.id_hospede.nome
        )

class Pagamento(models.Model):
    id_pagamento = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=50)
    data_pagamento = models.DateField()

    class Meta:
        managed = False
        db_table = 'pagamento'

    def __str__(self):
        return format_html(
            '<strong>Pagamento</strong> <ul><li>id: {}</li><li>valor: R${}</li><li>forma: {}</li><li>data: {}</li></ul>',
            self.id_pagamento,
            self.valor,
            self.forma_pagamento,
            self.data_pagamento
        )

class Quarto(models.Model):
    id_quarto = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'quarto'

    def __str__(self):
        return format_html(
            '<strong>Quarto</strong> <ul><li>numero: {}</li><li>preco: R${}</li></ul>',
            self.numero,
            self.preco
        )

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_quarto = models.ForeignKey(Quarto, models.DO_NOTHING, db_column='id_quarto')
    data_entrada = models.DateField()
    data_saida = models.DateField()
    tipo = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'reserva'

    def __str__(self):
        return format_html(
            '<strong>Reserva</strong> <ul><li>id: {}</li><li>tipo: {}</li><li>Quarto: {}</li><li>Entrada: {}</li><li>Saida: {}</li></ul>',
            self.id_reserva,
            self.tipo,
            self.id_quarto.numero,
            self.data_entrada,
            self.data_saida
        )

class ReservaPagamento(models.Model):
    id_reserva_pagamento = models.AutoField(primary_key=True)
    id_reserva = models.OneToOneField(Reserva, models.DO_NOTHING, db_column='id_reserva', blank=True, null=True)
    id_pagamento = models.OneToOneField(Pagamento, models.DO_NOTHING, db_column='id_pagamento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva_pagamento'

    def __str__(self):
        return format_html(
            '<strong>ReservaPagamento</strong> <ul><li>id: {}</li><li>Reserva: {}</li><li>Pagamento: {}</li></ul>',
            self.id_reserva_pagamento,
            self.id_reserva.id_reserva if self.id_reserva else 'N/A',
            self.id_pagamento.id_pagamento if self.id_pagamento else 'N/A'
        )

class ReservaServico(models.Model):
    id_reserva = models.OneToOneField(Reserva, models.DO_NOTHING, db_column='id_reserva', primary_key=True)
    id_servico = models.ForeignKey('Servico', models.DO_NOTHING, db_column='id_servico')

    class Meta:
        managed = False
        db_table = 'reserva_servico'
        unique_together = (('id_reserva', 'id_servico'),)

    def __str__(self):
        return format_html(
            '<strong>ReservaServico</strong> <ul><li>Reserva: {}</li><li>Servico: {}</li></ul>',
            self.id_reserva.id_reserva,
            self.id_servico.id_servico
        )

class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    refeicao_no_quarto = models.IntegerField()
    garagem = models.IntegerField()
    transporte_premium = models.IntegerField()
    minibar = models.IntegerField()
    spa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servico'

    def __str__(self):
        return format_html(
            '<strong>Servico</strong> <ul><li>id: {}</li><li>Refeicao: {}</li><li>Garagem: {}</li><li>Transporte: {}</li><li>Minibar: {}</li><li>Spa: {}</li></ul>',
            self.id_servico,
            self.refeicao_no_quarto,
            self.garagem,
            self.transporte_premium,
            self.minibar,
            self.spa
        )
