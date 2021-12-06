from django import forms
from django.core.mail.message import EmailMessage
from .models import Contato


class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'mensagem']

    def addcontato(self):
        contato_form = ContatoModelForm()
        contato = Contato()
        contato = contato_form.save(commit=False)
        contato.nome = self.cleaned_data['nome']
        contato.email = self.cleaned_data['email']
        contato.telefone = self.cleaned_data['telefone']
        contato.mensagem = self.cleaned_data['mensagem']
        contato.save()

'''
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email',max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=20)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'de: {nome}\n' \
                   f'{mensagem}'

        mail = EmailMessage(
            subject='contato: ' + nome,
            body=conteudo,
            from_email='contato@fabricasites.com.br',
            to=['contato@fabricasites.com.br',],
            headers={'Replay-To': email}
        )
        mail.send()

'''