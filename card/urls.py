from django.urls import path
from card.views import home, addCard, listCard, viewCard, updateCard, deleteCard
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    # Metodos utilizam CaseSensitive e nomenclaturas com intervalo de underscore
    path('card/add/', addCard, name="add_card"),
    path('card/list/', listCard, name="list_card"),
    path('card/<int:pk>/view/', viewCard, name="view_card"),
    path('card/<int:pk>/update/', updateCard, name="update_card"),
    path('card/<int:pk>/delete/', deleteCard, name="delete_card"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
