from django.urls import path, include  
from . import views
urlpatterns = [
    path('holamundo', views.hola_mundo, name="hola_mundo"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('articulos', views.articulos, name="articulos")
]