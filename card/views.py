from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from card.models import Card
from card.forms import AddCardForm


def home(request):
    return render(request, '01_home/index.html')


def addCard(request):
    if request.method == 'POST':
        form = AddCardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect(reverse_lazy('add_card'))
    else:
        form = AddCardForm()
    return render(request, '02_card/add.html', locals())


def listCard(request):
    cards = Card.objects.all()
    return render(request, '02_card/list.html', {'cards': cards})


def viewCard(request, pk):
    card = Card.objects.filter(id=pk).first()
    return render(request, '02_card/view.html', {'card': card})


def updateCard(request, pk):
    card = Card.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = AddCardForm(request.POST or None, request.FILES, instance=card)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect(reverse_lazy('add_card'))
    else:
        form = AddCardForm(instance=card)
    return render(request, '02_card/add.html', locals())


def deleteCard(request, pk):
    Card.objects.filter(id=pk).delete()
    cards = Card.objects.all()
    return render(request, '02_card/list.html', {'cards': cards})


# def addTerreno(request):
#     if request.method == 'POST':
#         form = AddTerrenoForm(request.POST, request.FILES)
#         if form.is_valid():
#             terreno = form.save(commit=False)
#             terreno.save()
#             return redirect(reverse_lazy('add_terreno'))
#     else:
#         form = AddTerrenoForm()
#     return render(request, '03_terreno/add-terreno.html', locals())
