from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_videojuego, name='ver_videojuego'),
    path('agregar/', views.agregar_videojuego, name='agregar_videojuego'),
    path('editar/<int:id>/', views.editar_videojuego, name='editar_videojuego'),
    path('borrar/<int:id>/', views.borrar_videojuego, name='borrar_videojuego'),
]