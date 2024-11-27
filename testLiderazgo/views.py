import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.shortcuts import render
from .models import Estudiante

# Create your views here.

def home(request):
    # Datos para Kurt Lewin
    liderazgos_kurt = {'Autoritario': 16, 'Democrático': 106,  'Laissez-Faire': 7}
    liderazgos_goleman = {'Afiliativo': 16, 'Autoritario': 6, ' Democrático': 41, 'Timonel': 4, 'Tutorial': 14, 'Visionario':47}
    localidad = {'Bolonchen': 7, 'Chanchen': 7, 'Crucero San Luis': 6, 'Cancabchen': 3,'Chanchen': 4,'Chun-Ek': 1, 'Chunchintok': 2, 
                 'Chunyaxnic':1, 'Crucero San Luis': 6, 'Dzemul': 1, 'Dzibalchén': 3, 'El Poste': 4, 'Emiliano Zapata': 1, 'Hopelchén': 52,
                  'ICH-EK':5, 'Iturbide': 4,'Katab': 1, 'Pachuitz':1, 'Pakchen': 1, 'Sahcabchén': 2, 'Suc-Tuc': 5, 'San Francisco de Campeche': 1,
                   'Santa Rita': 4, 'Tikinmul': 3, 'Ukum': 4, 'Xmejia': 8, 'Xcupil': 1, 'Xkan-ha': 1, 'Xmaben':3}
    
    genero = { 'Femenino': 68, 'Masculino': 60, 'Prefiero no decirlo': 1 }
    programEdu = { 'Ingeniería de innovación agrícola sustentable': 51, 'Ingeniería en sistemas computacionales':15, 'Licenciatura en administración':63 }


    # Serializamos los datos como JSON
    context = {
        'liderazgos_kurt': json.dumps(liderazgos_kurt),
        'liderazgos_goleman': json.dumps(liderazgos_goleman),
        'localidad': json.dumps(localidad),
        'genero': json.dumps(genero),
        'programEdu': json.dumps(programEdu)
    }
    return render(request, 'home.html', context)

def reporte(request):
    # Recuperar los filtros de la solicitud GET
    nombre = request.GET.get('nombre', '').strip()
    sexo = request.GET.get('sexo', '').strip()
    localidad = request.GET.get('localidad', '').strip()
    prepa_procedencia = request.GET.get('prepa', '').strip()
    semestre = request.GET.get('semestre', '').strip()
    programa = request.GET.get('programa', '').strip()
    institucion = request.GET.get('institucion', '').strip()
    kurt = request.GET.get('kurt', '').strip()
    goleman = request.GET.get('goleman', '').strip()

    # Filtrar los estudiantes según los parámetros ingresados
    estudiantes = Estudiante.objects.all()

    if nombre:
        estudiantes = estudiantes.filter(nombre__icontains=nombre)
    if semestre:
        estudiantes = estudiantes.filter(semestre__icontains=semestre)
    if programa:
        estudiantes = estudiantes.filter(programa_educativo__icontains=programa)
    if institucion:
        estudiantes = estudiantes.filter(institucion_educativa__icontains=institucion)
    if sexo:
        estudiantes = estudiantes.filter(sexo__icontains = sexo)
    if localidad:
        estudiantes = estudiantes.filter(localidad__icontains = localidad)
    if kurt:
        estudiantes = estudiantes.filter(liderazgo_kurt_lewin__icontains = kurt)
    if goleman:
        estudiantes = estudiantes.filter(liderazgo_daniel_goleman__icontains = goleman)
    if prepa_procedencia:
        estudiantes = estudiantes.filter(prepa_procedencia__icontains = prepa_procedencia)

        # Configurar el paginador
    paginator = Paginator(estudiantes, 5)  # Mostrar 10 registros por página
    page_number = request.GET.get('page')  # Obtener el número de la página actual desde la URL
    page_obj = paginator.get_page(page_number)  # Obtener los datos de la página correspondiente

    # Pasar los datos paginados al contexto
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'reporte.html', context,  )

def estadGen(request):
    liderazgos_kurt = (
        Estudiante.objects.values('liderazgo_kurt_lewin')
        .annotate(cantidad=Count('liderazgo_kurt_lewin'))
        .order_by('liderazgo_kurt_lewin')
    )

    # Agrupando y contando los tipos de liderazgo para Daniel Goleman
    liderazgos_goleman = (
        Estudiante.objects.values('liderazgo_daniel_goleman')
        .annotate(cantidad=Count('liderazgo_daniel_goleman'))
        .order_by('liderazgo_daniel_goleman')
    )

    genero = (
        Estudiante.objects.values('sexo')
        .annotate(cantidad=Count('sexo'))
        .order_by('sexo')
    )

    prograEdu = (
        Estudiante.objects.values('programa_educativo')
        .annotate(cantidad=Count('programa_educativo'))
        .order_by('programa_educativo')
    )

    context = {
        'liderazgos_kurt': liderazgos_kurt,
        'liderazgos_goleman': liderazgos_goleman,
        'sexo': genero,
        'programas':prograEdu

    }
    return render (request, 'estadisticasGenerales.html', context )

