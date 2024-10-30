from django.db import models
from django.contrib.auth.models import User

class Agendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendamentos')
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.descricao} em {self.data} às {self.hora}"

# Create your models here.
