from django.db import models
from django.core.exceptions import ValidationError


class Responsavel(models.Model):
    nome = models.CharField(
        max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(
        max_length=250, blank=False, null=False)

    def __str__(self):
        return self.nome


class Maquina(models.Model):
    modelo = models.CharField(
        max_length=250, blank=False, null=False)
    numero = models.CharField(
        'número', max_length=250, blank=False, null=False)

    def __str__(self):
        return f"{self.modelo} - {self.numero}"


class Oleo(models.Model):
    descricao = models.CharField(
        'descrição', max_length=250, blank=False, null=False)

    @property
    def quantidade(self):
        entrada = sum([e.quantidade for e in self.entradas.all()])
        saidas = sum([e.quantidade for e in self.saidas.all()])
        return entrada-saidas

    class Meta:
        verbose_name = 'Óleo'

    def __str__(self):
        return self.descricao


class EntradaOleo(models.Model):
    oleo = models.ForeignKey(
        Oleo, verbose_name='óleo', related_name='entradas', on_delete=models.CASCADE)
    quantidade = models.DecimalField(
        max_digits=10, decimal_places=2)
    nota_fiscal = models.CharField(
        'Número da nota fiscal', max_length=200, blank=False, null=False)
    data_entrada = models.DateField(
        'Data de entrada', blank=False, null=False)

    class Meta:
        verbose_name = 'Entrada de Óleo'

    def __str__(self):
        return f"Entrada de {self.quantidade} listros de {self.oleo.descricao}"


class SaidaOleo(models.Model):
    oleo = models.ForeignKey(
        Oleo, related_name='saidas', on_delete=models.CASCADE)
    quantidade = models.DecimalField(
        max_digits=10, decimal_places=2)
    maquina = models.ForeignKey(
        Maquina, related_name='oleos', on_delete=models.CASCADE)
    projeto = models.ForeignKey(
        Projeto, related_name='oleos', on_delete=models.CASCADE)
    responsavel = models.ForeignKey(
        Responsavel, related_name='oleos', on_delete=models.CASCADE)
    data_saida = models.DateField(
        'Data de saída', blank=False, null=False)

    class Meta:
        verbose_name = 'Saída de Óleo'

    def clean(self):
        if self.quantidade > self.oleo.quantidade:
            falta = self.quantidade - self.oleo.quantidade
            raise ValidationError(f'Quantidade insuficiente, falta {falta} listros')

    def __str__(self):
        return f"Saída de {self.quantidade} listros de {self.oleo.descricao}"
