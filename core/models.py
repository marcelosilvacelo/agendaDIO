from django.db import models
from django.contrib.auth.models import User#modulo usuario django
# Create your models here.
class Evento (models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null = True)
    data_evento = models.DateField(verbose_name= 'Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    #NOME DA TABELA A SER CRIADA
    class Meta:
        db_table = 'evento'
    # tratando o nome do evento exibindo o nome
    def __str__(self):
        return self.titulo