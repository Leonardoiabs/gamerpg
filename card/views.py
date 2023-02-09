from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from card.models import Card, Deck, DeckCard
from card.forms import AddCardForm, AddDeckForm, DeckAddCardForm


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


def addDeck(request):
    if request.method == 'POST':
        form = AddDeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.save()
            return redirect(reverse_lazy('list_deck'))
    else:
        form = AddDeckForm()
    return render(request, '02_card/deck/add.html', locals())


def listDeck(request):
    decks = Deck.objects.all()
    return render(request, '02_card/deck/list.html', {'decks': decks})


def viewDeck(request, pk):
    deck = Deck.objects.filter(id=pk).first()
    return render(request, '02_card/deck/view.html', {'deck': deck})


def updateDeck(request, pk):
    deck = Deck.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = AddDeckForm(request.POST or None, instance=deck)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.save()
            return redirect(reverse_lazy('add_deck'))
    else:
        form = AddDeckForm(instance=deck)
    return render(request, '02_card/deck/add.html', locals())


def deleteDeck(request, pk):
    Deck.objects.filter(id=pk).delete()
    decks = Deck.objects.all()
    return render(request, '02_card/deck/list.html', {'decks': decks})


def deckAddCards(request, pk_deck):
    cartas_disponiveis = Card.objects.all()
    deck = Deck.objects.filter(id=pk_deck).first()
    cartas_do_deck = deck.deckcard_set.all().values_list('card_id', flat=True)

    if request.method == 'POST':
        form = DeckAddCardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if not deck.deckcard_set.filter(card=form.card).exists():
                if deck.deckcard_set.all().count() < 6:
                    form.deck = deck
                    form.save()
            else:
                deck.deckcard_set.filter(card=form.card).delete()
            return redirect(reverse('deck_add_cards', args=[deck.id]))
    else:
        form = DeckAddCardForm()
    return render(request, '02_card/deck/add_card.html', locals())
