from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic import FormView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import CarrosselContainer, ProdutosSerralheria, Contato
from .forms import ContatoModelForm
from .utils import render_to_pdf
from django.shortcuts import redirect


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['imagens'] = CarrosselContainer.objects.all()
        context['serralheria'] = ProdutosSerralheria.objects.filter(destaques=True)
        return context

class SobreNosView(TemplateView):
    template_name = 'sobre_nos.html'


class ContatoView(FormView):
    template_name = 'contato.html'
    form_class = ContatoModelForm
    success_url = reverse_lazy('contato')

    def form_valid(self, form, *args, **kwargs):
        form.addcontato()
        messages.success(self.request, 'Contato salvo com sucesso!!\n\nRetornaremos o mais rápido possível')
        return super(ContatoView, self).form_valid(form, *args, *kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao salvar contato!!')
        return super(ContatoView, self).form_invalid(form, *args, *kwargs)

class ProdutoView(TemplateView):
    template_name = 'produtos.html'

    def get_context_data(self, **kwargs):
        context = super(ProdutoView, self).get_context_data(**kwargs)
        context['serralheria'] = ProdutosSerralheria.objects.all()
        return context

class ProdutoViewPdf(View):

    def get(self, request, *args, **kwargs):
        produtos = ProdutosSerralheria.objects.all()
        data = {
            'serralheria': produtos
        }
        pdf = render_to_pdf('produtospdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class AcessoNegado(TemplateView):
    template_name = 'negado.html'

class ContatosViewPdf(View):
    def get(self, request, *args, **kwargs):
        contatos = Contato.objects.all()
        data = {
            'contatos': contatos,
            'count': contatos.count()
        }
        if request.user != 'AnonymousUser':
            pdf = render_to_pdf('contatospdf.html', data)
            return HttpResponse(pdf, content_type='application/pdf')
        else:
            return redirect('negado')


class ContainerView(TemplateView):
    template_name = 'container.html'

    def get_context_data(self, **kwargs):
        context = super(ContainerView, self).get_context_data(**kwargs)
        context['container'] = CarrosselContainer.objects.all()
        return context