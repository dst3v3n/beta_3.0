from django.shortcuts import render

# Create your views here.

class vista:

    def crear(request):
        return render (request, 'crearrequisicion.html')

    def ver(request):
        return render (request, 'verrequisicion.html')
    
    def ofertascy(request):
        return render (request, 'veroferta.html')
    
    def ofertaszp(request):
        return render (request, 'ofertazp.html')