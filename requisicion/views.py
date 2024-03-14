from django.shortcuts import render

# Create your views here.

class vista:

    def crear(request):
        return render (request, 'crearrequisicion.html')

    def ver(request):
        return render (request, 'verrequisicion.html')