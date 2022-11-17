from django.urls import path
from App.views import inicio,formularioFiccion,formularioTerror,formularioNovela,buscar_editorial,buscar_genero_terror

urlpatterns = [
    path('inicio/', inicio, name = "Inicio"),
    path('ficcion/', formularioFiccion , name = "Ficcion"),
    path('terror/', formularioTerror, name = "Terror"),
    path('novela/', formularioNovela , name = "Novela"),
    path('busquedaEditorial/', buscar_editorial, name = "Editor"),
    path('buscarTerror/', buscar_genero_terror, name = "Gterror"),

]

