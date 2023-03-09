from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length= 50)
    endereco = models.CharField(max_length= 50)
    idade = models.IntegerField()

    def _str_(self):
        return self.nome

