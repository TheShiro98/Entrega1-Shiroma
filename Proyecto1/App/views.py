from django.shortcuts import render
from App.models import Ficcion,Terror,Novela
# Create your views here.

def genero_ficcion(request):
    f1 = Ficcion(
        nombre = 'Sarah L.',
        apellido = 'Mass', 
        edad = 25,
        titulo = 'Trono de Cristal',
        genero = 'Ficción',
        editorial = 'Alfaguara',
        fecha = '2017-02-4'
    )
    return render(request,'ficcion.html',{'fic':[f1]})


def genero_terror(request):
    t1 = Terror(
        nombre = 'Nic',
        apellido = 'Sheff', 
        edad = 30,
        titulo = 'Harmony House',
        genero = 'Terror',
        editorial = 'V&R',
        fecha = '2010-09-21'
    )
    return render(request,'terror.html',{'ter':[t1]})


def genero_novela(request):
    n1 = Novela(
        nombre = 'Phyllis C.',
        apellido = 'Cast', 
        edad = 50,
        titulo = 'Elegida por la luna',
        genero = 'Novela',
        editorial = 'Alfaguara',
        fecha = '2016-06-18'
    )
    return render(request,'novela.html',{'nov':[n1]})
