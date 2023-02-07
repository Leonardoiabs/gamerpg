from django.contrib import admin
from card.models import Tipo, Deck, Card, DeckCard


admin.site.register(Tipo)
admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(DeckCard)