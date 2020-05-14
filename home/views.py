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
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']

            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)
        else:
            return render(request, self.template_name, {'form': form})


def port(requests):
    ip = "google.com"
    ports =[21, 22, 23, 25, 80, 135, 8080, 443, 3306] #21=FTP, 22=SSH, 23=TELNET, 25=SMTP, 3306=MSQL

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET conecta no dominio da internet
        #sock_stream expecifica que é o TCP
        client.settimeout(0.2)#tempo que vai testar cada conexão
        code = client.connect_ex((ip, port)) #diz o site quer quer conectar e a porta

        if code == 0:
            print ("{} -> porta aberta".format(port))

    print ("Scan finalizado")