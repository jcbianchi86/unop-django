from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Docente
from .forms import DocenteForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

@login_required
def inicio(request):
    return render(request, 'gestion/inicio.html')

@login_required
def lista_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'gestion/lista_docentes.html', {'docentes': docentes})

@login_required
def agregar_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_docentes')
    else:
        form = DocenteForm()
    return render(request, 'gestion/agregar_docente.html', {'form': form})

@login_required
def eliminar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.delete()
        return redirect('lista_docentes')
    return render(request, 'gestion/eliminar_docente.html', {'docente': docente})