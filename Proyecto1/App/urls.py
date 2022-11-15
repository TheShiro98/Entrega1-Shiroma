from django.urls import path
from App.views import genero_ficcion,genero_terror,genero_novela

urlpatterns = [
    path('ficcion/', genero_ficcion),
    path('terror/', genero_terror),
    path('novela/', genero_novela)
]