from django.contrib import admin
from core.models import Evento

# Register your models here.
#classe que mostra os campos do evento
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','data_evento','data_criacao')
    #FILTRO DE BUSCA necessario virgula
    list_filter = ('usuario','data_evento')

admin.site.register(Evento, EventoAdmin)


