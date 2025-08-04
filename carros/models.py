from django.db import models

# Create your models here.


class Marca(models.Model):
    idmarca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)


    # def __str__(self): retorna o valor que vai ser mostrado na tela
    def __str__(self):
        return self.marca


class Carro(models.Model):
    idcarro = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100)
    idmarca = models.ForeignKey(Marca, on_delete=models.PROTECT,related_name='carros_marca',null=True, blank=True)
    cor = models.CharField(max_length=100)
    ano = models.IntegerField(blank=True, null=True)
    anofabricacao = models.IntegerField(blank=True, null=True)
    placa = models.CharField(max_length=30, null=True, blank=True)
    foto = models.ImageField(upload_to='carros/fotos/', null=True, blank=True)


    def __str__(self):
        
        return self.modelo
    

