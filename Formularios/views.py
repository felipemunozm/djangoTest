from django.shortcuts import render

# Create your views here
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from .models import Pregunta

def index(request):
    lista_ultima_pregunta = Pregunta.objects.order_by('-fecha_publicacion')[:5]
    salida = ', '.join([p.texto_pregunta for p in lista_ultima_pregunta])
    return render(request,'formulario/index.html',{'lista_ultima_pregunta': lista_ultima_pregunta})

def detalle(request, id_pregunta):
    try:
        pregunta = Pregunta.objects.get(pk=id_pregunta)
    except Pregunta.DoesNotExists:
        raise Http404("La pregunta no existe")
    return render(request, 'formulario/detalle.html',{'pregunta':pregunta})

def resultado(request, id_pregunta):
    pregunta = get_object_or_404(Pregunta, pk=id_pregunta)
    return render(request, 'formulario/resultados.html', {'pregunta': pregunta})

def votar(request, id_pregunta):
    pregunta = get_object_or_404(Pregunta, pk=id_pregunta)
    try:
        alternativa_seleccionada = pregunta.alternativa_set.get(pk=request.POST['alternativa'])
    except (KeyError, Alternativa.DoesNotExists):
        return render(request, 'formulario/detalle.html', {'pregunta': pregunta, 'mensaje_error':'NO hay alternativa seleccionada'})
    else:
        alternativa_seleccionada.votos += 1
        alternativa_seleccionada.save()
        return HttpResponseRedirect(reverse('formulario:resultados',args=(pregunta.id,)))
