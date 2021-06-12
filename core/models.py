from django.db import models

from stdimage.models import StdImageField

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)


    class Meta:
        abstract = True


class CarrosselContainer(Base):
    descricao = models.CharField('Descrição', max_length=50)
    imagem = StdImageField('Imagem', upload_to='carrossel_Cont')
    destaques = models.BooleanField('Destaque?', default=False)


    class Meta:
        verbose_name = 'imagem'
        verbose_name_plural = 'imagens'


class TipoProdutoLoc(models.Model):
    tipo = models.CharField('Tipo', max_length=50)


class ProdutosSerralheria(Base):
    #STATUS_CHOICES = (
     #   ('pertence_ao_index', 'Pertence_ao_Index'),
      #  ('não_pertence_ao_index', 'Não_Pertence_ao_Index')
    #)
    prod = models.ForeignKey(TipoProdutoLoc, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    imagem = StdImageField('Imagem', upload_to='Produtos_Serralheria', variations={'thumb': {'width': 500, 'height': 250, 'crop': False}})
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    #status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='não_pertence_ao_index')
    destaques = models.BooleanField('Destaque?', default=False)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome




