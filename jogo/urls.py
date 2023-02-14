from django.urls import path
from jogo.views import home, addJogador, listJogador, viewJogador, updateJogador, deleteJogador, partidaAddDeck
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('jogador/add/', addJogador, name="add_jogador"),
    path('jogador/list/', listJogador, name="list_jogador"),
    path('jogador/<int:pk>/view/', viewJogador, name="view_jogador"),
    path('jogador/<int:pk>/update/', updateJogador, name="update_jogador"),
    path('jogador/<int:pk>/delete/', deleteJogador, name="delete_jogador"),

    path('partida/add_deck/', partidaAddDeck, name="add_deck_partida"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
