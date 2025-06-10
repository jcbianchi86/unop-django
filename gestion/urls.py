from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta raíz de la app
    path('docentes/', views.lista_docentes, name='lista_docentes'),
    path('docentes/agregar/', views.agregar_docente, name='agregar_docente'),
    path('docentes/eliminar/<int:pk>/', views.eliminar_docente, name='eliminar_docente'),
]
