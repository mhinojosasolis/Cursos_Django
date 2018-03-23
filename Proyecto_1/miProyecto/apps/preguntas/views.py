
from django.http import HttpResponse
from apps.preguntas.models import Pregunta
from django.shortcuts import get_object_or_404, render_to_response


# Create your views here.

def index(request):
    preguntas = Pregunta.objects.all()
    return render_to_response('preguntas/index',{'preguntas':preguntas})


def pregunta_detalle(request, pregunta_id):
        pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
        return render_to_response('preguntas',{'pregunta':pregunta})

