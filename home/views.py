from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from home.forms import HomeForm
import socket


class homeView(TemplateView):
    template_name = 'home.html'

    def home (self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post (self, request):
        ports = [21, 22, 23, 25, 80, 135, 8080, 443, 3306]
        portas_abertas = []
        form = HomeForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data['post']
            for port in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.2)  # tempo que vai testar cada conexão
                code = client.connect_ex((ip, port))  # diz o site quer quer conectar e a porta
                if code == 0:
                    portas_abertas.append(port)
            text = form.cleaned_data['post']
            args = {'form': form, 'text': text, 'portas_abertas': portas_abertas}
            return render(request, self.template_name, args)
        else:
            return render(request, self.template_name, {'form': form})

