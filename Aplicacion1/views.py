from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "Aplicacion1/index.html")

def jugadores(request):
    contexto = {'jugadores':Jugador.objects.all()}
    return render(request, "Aplicacion1/jugadores.html", contexto)

def personajes(request):
    contexto = {'personajes':Personaje.objects.all()}
    return render(request, "Aplicacion1/personajes.html", contexto)

def talentos(request):
    contexto = {'talentos':Talento.objects.all()}
    return render(request, "Aplicacion1/talentos.html", contexto)

# Forms
def jugadoresform(request):
    if request.method == "POST":
        #2da o n vez
        miForm = JugadoresForm(request.POST)
        if miForm.is_valid():
            jugador_nombre = miForm.cleaned_data.get("nombre")
            jugador_apellido = miForm.cleaned_data.get("apellido")
            jugador_email = miForm.cleaned_data.get("email")
            jugador= Jugador(nombre = jugador_nombre, apellido = jugador_apellido, email = jugador_email)
            jugador.save()
            return render(request, "Aplicacion1/jugadores.html")
    else:
        miForm = JugadoresForm()
    return render (request, "Aplicacion1/jugadoresform.html", {"form":miForm})

def personajesform(request):
    if request.method == "POST":
        #2da o n vez
        miForm = PersonajesForm(request.POST)
        if miForm.is_valid():
            personaje_nombre = miForm.cleaned_data.get("nombre")
            personaje= Personaje(nombre = personaje_nombre)
            personaje.save()
            return render(request, "Aplicacion1/personajes.html")
    else:
        miForm = PersonajesForm()
    return render (request, "Aplicacion1/personajesform.html", {"form":miForm})

def talentosform(request):
    if request.method == "POST":
        #2da o n vez
        miForm = TalentosForm(request.POST)
        if miForm.is_valid():
            talento_nombre = miForm.cleaned_data.get("nombre")
            talento= Talento(nombre = talento_nombre)
            talento.save()
            return render(request, "Aplicacion1/talentos.html")
    else:
        miForm = TalentosForm()
    return render (request, "Aplicacion1/talentosform.html", {"form":miForm})

def buscarjugador(request):
    return render(request, "Aplicacion1/buscarjugador.html")

def encontrarjugador(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        jugador = Jugador.objects.filter(nombre__icontains=patron)
        contexto = {"jugador":jugador}
        return render(request, "Aplicacion1/jugadores.html", contexto)
    else:
         contexto = {'jugadores':Jugador.objects.all()}
         return render(request, "Aplicacion1/jugadores.html", contexto)
    
    
