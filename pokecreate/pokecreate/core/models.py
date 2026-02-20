from django.db import models

# Create your models here.


class Pokemon(models.Model):
    nome : str = models.CharField(max_length=100)
    categoria : str = models.CharField(max_length=25)
    descricao : str = models.CharField(max_length=10000)
    data_criacacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateField(auto_now=True)


    def __str__(self):
        return self.nome
    
class Usuarios(models.Model):
    nome: str = models.CharField(max_length=100)
    descricao : str = models.CharField(max_length=10000)
    data_criacacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateField(auto_now=True)
    email : str = models.CharField(max_length=100)
    senha: str = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    

    


