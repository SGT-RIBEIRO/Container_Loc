# Generated by Django 3.2.4 on 2021-06-11 01:32

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarrosselContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('imagem', stdimage.models.StdImageField(upload_to='carrossel_Cont', verbose_name='Imagem')),
                ('destaques', models.BooleanField(default=False, verbose_name='Destaque?')),
            ],
            options={
                'verbose_name': 'imagem',
                'verbose_name_plural': 'imagens',
            },
        ),
        migrations.CreateModel(
            name='TipoProdutoLoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='ProdutosSerralheria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(upload_to='Produtos_Serralheria', verbose_name='Imagem')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('destaques', models.BooleanField(default=False, verbose_name='Destaque?')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoprodutoloc')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]