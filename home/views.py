from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from home.forms import HomeForm
import socket

#antes fazia as views só com funções, mas usar classe para facilitar, Então tanto faz.
class homeView(TemplateView):
    template_name = 'home.html'

    #função get e post têm que ter esse nome por padão do django
    def get (self, request):
        form = HomeForm() #criando um formulário vazio
        return render(request, self.template_name, {'form': form}) #retornando a página html e o formulário criado

    def post (self, request):
        ports = [21, 22, 23, 25, 80, 135, 8080, 443, 3306]#algumas portas importantes 21=FTP, 22=SSH, 23=TELNET, 25=SMTP, 3306=MSQL
        portas_abertas = []
        form = HomeForm(request.POST)#método pra quando o formulário for requisitado
        try:
            form.is_valid()
            ip = form.cleaned_data['post']#deixando a variável igual ao que a pessoa escreveu em forma de string
            for port in ports:
                # AF_INET conecta no dominio da internet
                # sock_stream expecifica que é o TCP
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.2)  # tempo que vai testar cada conexão
                code = client.connect_ex((ip, port))  # diz o site quer quer conectar e a porta
                if code == 0:
                    portas_abertas.append(port)
            text = form.cleaned_data['post']
            form = HomeForm()
            args = {'form': form, 'text': text, 'portas_abertas': portas_abertas}
            return render(request, self.template_name, args)
        except:
            resposta_errada=True
            return render(request, self.template_name, {'form': form, 'resposta_errada': resposta_errada})

