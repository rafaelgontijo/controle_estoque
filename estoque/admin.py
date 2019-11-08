from django.contrib import admin
from .models import Oleo, Projeto, EntradaOleo, SaidaOleo, Responsavel, Maquina


class OleoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'quantidade')


class MaquinaAdmin(admin.ModelAdmin):
    pass


class ProjetoAdmin(admin.ModelAdmin):
    pass


class EntradaOleoAdmin(admin.ModelAdmin):
    list_display = ('oleo', 'quantidade', 'nota_fiscal', 'data_entrada')
    list_filter = ('oleo', 'nota_fiscal', 'data_entrada')


class SaidaOleoAdmin(admin.ModelAdmin):
    list_display = ('oleo', 'quantidade', 'maquina', 'projeto', 'responsavel', 'data_saida')
    list_filter = ('oleo', 'maquina', 'projeto', 'responsavel', 'data_saida')


class ResponsavelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Oleo, OleoAdmin)
admin.site.register(Maquina, MaquinaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(EntradaOleo, EntradaOleoAdmin)
admin.site.register(SaidaOleo, SaidaOleoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
