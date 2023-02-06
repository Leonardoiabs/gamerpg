from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from jogo.models import Jogador
from jogo.forms import AddJogadorForm


def home(request):
    return render(request, '01_home/index.html')


def addJogador(request):
    if request.method == 'POST':
        form = AddJogadorForm(request.POST, request.FILES)
        if form.is_valid():
            jogador = form.save(commit=False)
            jogador.save()
            return redirect(reverse_lazy('add_jogador'))
    else:
        form = AddJogadorForm()
    return render(request, '04_jogo/jogador/add.html', locals())


def listJogador(request):
    jogadores = Jogador.objects.all()
    return render(request, '04_jogo/jogador/list.html', {'jogadores': jogadores})


def viewJogador(request, pk):
    jogador = Jogador.objects.filter(id=pk).first()
    return render(request, '04_jogo/jogador/view.html', {'jogador': jogador})


def updateJogador(request, pk):
    jogador = Jogador.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = AddJogadorForm(request.POST or None, request.FILES, instance=jogador)
        if form.is_valid():
            jogador = form.save(commit=False)
            jogador.save()
            return redirect(reverse_lazy('add_jogador'))
    else:
        form = AddJogadorForm(instance=jogador)
    return render(request, '04_jogo/jogador/add.html', locals())


def deleteJogador(request, pk):
    Jogador.objects.filter(id=pk).delete()
    jogadores = Jogador.objects.all()
    return render(request, '04_jogo/jogador/list.html', {'jogadores': jogadores})
