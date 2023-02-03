from django.urls import path
from terreno.views import addTerreno, listTerreno, viewTerreno, updateTerreno, deleteTerreno
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/', addTerreno, name="add_terreno"),
    path('list/', listTerreno, name="list_terreno"),
    path('<int:pk>/view/', viewTerreno, name="view_terreno"),
    path('<int:pk>/update/', updateTerreno, name="update_terreno"),
    path('<int:pk>/delete/', deleteTerreno, name="delete_terreno"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
