from django import forms


class Formulario_Ficcion(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido =forms.CharField(max_length=40)
    edad =forms.IntegerField()
    titulo =forms.CharField(max_length=40)
    genero =forms.CharField(max_length=40)
    editorial =forms.CharField(max_length=40)
    fecha =forms.DateField()


class Formulario_Terror(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido =forms.CharField(max_length=40)
    edad =forms.IntegerField()
    titulo =forms.CharField(max_length=40)
    genero =forms.CharField(max_length=40)
    editorial =forms.CharField(max_length=40)
    fecha =forms.DateField()


class Formulario_Novela(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido =forms.CharField(max_length=40)
    edad =forms.IntegerField()
    titulo =forms.CharField(max_length=40)
    genero =forms.CharField(max_length=40)
    editorial =forms.CharField(max_length=40)
    fecha =forms.DateField()