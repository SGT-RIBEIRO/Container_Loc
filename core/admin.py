from django.contrib import admin
from .models import CarrosselContainer, ProdutosSerralheria,TipoProdutoLoc

@admin.register(CarrosselContainer)
class CarrosselAdmin(admin.ModelAdmin):
    list_display = ('criados', 'modificado', 'ativo', 'imagem')

@admin.register(ProdutosSerralheria)
class ProdutosSerralheriaAdmin(admin.ModelAdmin):
    list_display = ('criados', 'modificado', 'ativo','destaques', 'nome', 'imagem', 'preco')
    raw_id_fields = ('prod',)

@admin.register(TipoProdutoLoc)
class TipoProdutoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)




