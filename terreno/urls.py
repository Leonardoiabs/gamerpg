from django.urls import path
from terreno.views import addTerreno, listTerreno, viewTerreno, updateTerreno, deleteTerreno
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('terreno/add/', addTerreno, name="add_terreno"),
    path('terreno/list/', listTerreno, name="list_terreno"),
    path('terreno/<int:pk>/view/', viewTerreno, name="view_terreno"),
    path('terreno/<int:pk>/update/', updateTerreno, name="update_terreno"),
    path('terreno/<int:pk>/delete/', deleteTerreno, name="detele_terreno"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
