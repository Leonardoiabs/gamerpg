from django.urls import path
from card.views import (
    home, addCard, listCard, viewCard, updateCard, deleteCard, addDeck, listDeck, viewDeck, updateDeck, deleteDeck,
    deckAddCards
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('card/add/', addCard, name="add_card"),
    path('card/list/', listCard, name="list_card"),
    path('card/<int:pk>/view/', viewCard, name="view_card"),
    path('card/<int:pk>/update/', updateCard, name="update_card"),
    path('card/<int:pk>/delete/', deleteCard, name="delete_card"),

    path('deck/add/', addDeck, name="add_deck"),
    path('deck/list/', listDeck, name="list_deck"),
    path('deck/<int:pk>/view/', viewDeck, name="view_deck"),
    path('deck/<int:pk>/update/', updateDeck, name="update_deck"),
    path('deck/<int:pk>/delete/', deleteDeck, name="delete_deck"),
    path('deck/<int:pk_deck>/add/cards/', deckAddCards, name="deck_add_cards"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
