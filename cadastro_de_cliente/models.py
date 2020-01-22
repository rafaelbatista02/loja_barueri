from django.db import models

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.IntegerField()
    cpf = models.IntegerField()
    email = models.EmailField()
    nascimento = models.IntegerField()
    idade =  models.IntegerField()

    def __str__(self):
        return self.nome



    