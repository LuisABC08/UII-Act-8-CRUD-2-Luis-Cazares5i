# app_videojuego/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Videojuego  # Importa tu modelo Videojuego

# Listar videojuegos (Corresponde a la URL con name='inicio')
def index(request): # Renombramos a 'index' para que coincida con views.index en urls.py
    videojuegos = Videojuego.objects.all()
    # Usamos 'listar_videojuegos.html' como nombre de plantilla, puedes cambiarlo si tienes otro.
    return render(request, 'listar_videojuegos.html', {'videojuegos': videojuegos})

# Ver detalles de un videojuego (Corresponde a la URL con name='ver_videojuego')
def ver_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, pk=id)
    # Usamos 'ver_videojuego.html' como nombre de plantilla.
    return render(request, 'ver_videojuego.html', {'videojuego': videojuego})

# Agregar un nuevo videojuego (Corresponde a la URL con name='agregar_videojuego')
def agregar_videojuego(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        desarrollador = request.POST['desarrollador']
        genero = request.POST['genero']
        plataforma = request.POST['plataforma']
        fecha_lanzamiento = request.POST['fecha_lanzamiento']
        
        Videojuego.objects.create(
            titulo=titulo,
            desarrollador=desarrollador,
            genero=genero,
            plataforma=plataforma,
            fecha_lanzamiento=fecha_lanzamiento
        )
        return redirect('inicio') # Redirige a 'inicio' (la lista de videojuegos)
    # Usamos 'agregar_videojuego.html' como nombre de plantilla.
    return render(request, 'agregar_videojuego.html')

# Editar un videojuego existente (Corresponde a la URL con name='editar_videojuego')
def editar_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, pk=id)
    if request.method == 'POST':
        videojuego.titulo = request.POST['titulo']
        videojuego.desarrollador = request.POST['desarrollador']
        videojuego.genero = request.POST['genero']
        videojuego.plataforma = request.POST['plataforma']
        videojuego.fecha_lanzamiento = request.POST['fecha_lanzamiento']
        videojuego.save()
        return redirect('inicio') # Redirige a 'inicio' (la lista de videojuegos)
    # Usamos 'editar_videojuego.html' como nombre de plantilla.
    return render(request, 'editar_videojuego.html', {'videojuego': videojuego})

# Borrar un videojuego (Corresponde a la URL con name='borrar_videojuego')
def borrar_videojuego(request, id):
    videojuego = get_object_or_404(Videojuego, pk=id)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('inicio') # Redirige a 'inicio' (la lista de videojuegos)
    # Usamos 'borrar_videojuego.html' como nombre de plantilla.
    return render(request, 'borrar_videojuego.html', {'videojuego': videojuego})