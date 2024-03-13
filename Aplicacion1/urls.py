from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('jugadores/', jugadores, name="jugadores"),
    path('personajes/', personajes, name="personajes"),
    path('talentos/', talentos, name="talentos"),
    path('admin/', admin.site.urls),
    # Forms
    path('jugadoresform/', jugadoresform, name="jugadoresform"),
    path('talentosform/', talentosform, name="talentosform"),
    path('personajesform/', personajesform, name="personajesform"),
    #busqueda
    path('buscarjugador/', buscarjugador, name="buscarjugador"),
    path('encontrarjugador/', encontrarjugador, name="encontrarjugador"),


]
