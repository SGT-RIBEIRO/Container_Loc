from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import CarrosselContainer, ProdutosSerralheria
from .forms import ContatoForm


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
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso!!')
        return super(ContatoView, self).form_valid(form, *args, *kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o email!!')
        return super(ContatoView, self).form_invalid(form, *args, *kwargs)

class ProdutoView(TemplateView):
    template_name = 'produtos.html'

    def get_context_data(self, **kwargs):
        context = super(ProdutoView, self).get_context_data(**kwargs)
        context['serralheria'] = ProdutosSerralheria.objects.all()
        return context

class ContainerView(TemplateView):
    template_name = 'container.html'

    def get_context_data(self, **kwargs):
        context = super(ContainerView, self).get_context_data(**kwargs)
        context['container'] = CarrosselContainer.objects.all()
        return context