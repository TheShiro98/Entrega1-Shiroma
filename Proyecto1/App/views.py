from django.shortcuts import render
from django.http import HttpResponse
from App.models import Ficcion,Terror,Novela
from App.forms import Formulario_Ficcion,Formulario_Novela,Formulario_Terror

# Create your views here.

def inicio(request):

    return render(request, "index.html")


#def genero_ficcion(request):
#    f1 = Ficcion(
#        nombre = 'Sarah L.',
#        apellido = 'Mass', 
#        edad = 25,
#        titulo = 'Trono de Cristal',
#        genero = 'Ficción',
#        editorial = 'Alfaguara',
#        fecha = '2017-02-4'
#    )
#    return render(request,'ficcion.html',{'fic':[f1]})


#def genero_terror(request):
#    t1 = Terror(
#        nombre = 'Nic',
#        apellido = 'Sheff', 
#        edad = 30,
#        titulo = 'Harmony House',
#        genero = 'Terror',
#        editorial = 'V&R',
#        fecha = '2010-09-21'
#    )
#    return render(request,'terror.html',{'ter':[t1]})


#def genero_novela(request):
#    n1 = Novela(
#        nombre = 'Phyllis C.',
#        apellido = 'Cast', 
#        edad = 50,
#        titulo = 'Elegida por la luna',
#        genero = 'Novela',
#        editorial = 'Alfaguara',
#        fecha = '2016-06-18'
#    )
#    return render(request,'novela.html',{'nov':[n1]})







def formularioFiccion(request):

    if request.method == 'POST':

        miFormulario = Formulario_Ficcion(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            f1 = Ficcion(
            nombre = informacion['nombre'],
            apellido = informacion['apellido'], 
            edad = informacion['edad'],
            titulo = informacion['titulo'],
            genero = informacion['genero'],
            editorial = informacion['editorial'],
            fecha = informacion['fecha']
            )

            f1.save()

            return render(request,'index.html')
    
    else:

        miFormulario = Formulario_Ficcion()

    return render(request,"ficcion.html", {"miFormulario":miFormulario})



def formularioTerror(request):

    if request.method == 'POST':

        miFormulario = Formulario_Terror(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            f1 = Terror(
            nombre = informacion['nombre'],
            apellido = informacion['apellido'], 
            edad = informacion['edad'],
            titulo = informacion['titulo'],
            genero = informacion['genero'],
            editorial = informacion['editorial'],
            fecha = informacion['fecha']
            )

            f1.save()

            return render(request,'index.html')
    
    else:

        miFormulario = Formulario_Terror()

    return render(request,"terror.html", {"miFormulario":miFormulario})



def formularioNovela(request):

    if request.method == 'POST':

        miFormulario = Formulario_Novela(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            f1 = Novela(
            nombre = informacion['nombre'],
            apellido = informacion['apellido'], 
            edad = informacion['edad'],
            titulo = informacion['titulo'],
            genero = informacion['genero'],
            editorial = informacion['editorial'],
            fecha = informacion['fecha']
            )

            f1.save()

            return render(request,'index.html')
    
    else:

        miFormulario = Formulario_Novela()

    return render(request,"novela.html", {"miFormulario":miFormulario})



#----------------------------#


def buscar_editorial(request):

    if request.GET.get('editorial',False):
        editorial = request.GET['editorial']
        ficcion = Ficcion.objects.filter(editorial__icontains=editorial)

        return render(request,'busquedaEditorial.html',{'ficcion':ficcion})

    else:
        respuesta = 'No hay datos'

    return render(request, 'busquedaEditorial.html',{'resupuesta':respuesta})