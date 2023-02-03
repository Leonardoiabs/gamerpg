from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from terreno.models import Terreno
from terreno.forms import AddTerrenoForm


def addTerreno(request):
    if request.method == 'POST':
        form = AddTerrenoForm(request.POST, request.FILES)
        if form.is_valid():
            terreno = form.save(commit=False)
            terreno.save()
            return redirect(reverse_lazy('add_terreno'))
    else:
        form = AddTerrenoForm()
    return render(request, '03_terreno/add.html', locals())


def listTerreno(request):
    terreno = Terreno.objects.all()
    return render(request, '03_terreno/list.html', {'terrenos': terreno})


def viewTerreno(request, pk):
    terreno = Terreno.objects.filter(id=pk).first()
    return render(request, '03_terreno/view.html', {'terreno': terreno})


def updateTerreno(request, pk):
    terreno = Terreno.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = AddTerrenoForm(request.POST or None, request.FILES, instance=terreno)
        if form.is_valid():
            terreno = form.save(commit=False)
            terreno.save()
            return redirect(reverse_lazy('add_terreno'))
        else:
            form = AddTerrenoForm(instance=terreno)
        return render(request, '03_terreno/add.html', locals())


def deleteTerreno(request, pk):
    Terreno.objects.filter(id=pk).delete()
    terreno = Terreno.objects.all()
    return render(request, '03_terreno/list.html', {'terrenos': terreno})
