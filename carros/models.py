from django.db import models

# Create your models here.

class Carro(models.Model):
    idcarro = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField(blank=True, null=True)
    anofabricacao = models.IntegerField(blank=True, null=True)
