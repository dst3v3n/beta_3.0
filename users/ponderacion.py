# from googlemaps import Client
# import os
# from HojaVida.models import Experience , Education
# from requisicion.models import Requisicion
# from datetime import datetime

# def ubicacion (origen , destino):
#     client = Client(os.environ['GOOGLE_MAPS_API_KEY'])
#     distance = client.distance_matrix(origen, destino)['rows'][0]['elements'][0]['distance']['text']
#     return puntaje_ubicacion(distance)

# def experiencia (id:int):
#     suma = 0
#     meses = Experience.objects.filter(id_myuser_id = id).values("start_date" , "end_date")
#     for i in meses:
#         fecha_inicio = datetime(i["start_date"].year , i["start_date"].month , i["start_date"].day)
#         fecha_fin = datetime(i["end_date"].year , i["end_date"].month , i["end_date"].day)

#         diferencia = fecha_fin - fecha_inicio
#         meses_experiencia = diferencia.days / 30
#         meses_experiencia = round(meses_experiencia)
#         suma += meses_experiencia
#     return suma

# def educacion (id_oferta , id_usuario):
#     nombre_company = Requisicion.objects.filter (id = id_oferta) .values ("educacion" , "profesion")
#     nombre_company = nombre_company[0]
#     educacion = nombre_company["educacion"]
#     nombre_profesion = nombre_company["profesion"]
#     palabras = palabras_claves(nombre_profesion)
#     nombre_educacion = Education.objects.filter (id_myuser_id = id_usuario).values ("name_course" , "educational_level")
#     cursos_coincidentes = []

#     for curso in nombre_educacion:
#         nombre_curso_minusculas = curso["name_course"].lower()
#         if any(palabra.lower() in nombre_curso_minusculas for palabra in palabras):
#             cursos_coincidentes.append(([curso["educational_level"] , curso["name_course"]]))
#     educativo = nivel_educativo (educacion , cursos_coincidentes)

# def palabras_claves (texto:str):
#     lista = ["y" , "de" , "en" , "a" , "la" , "del" , "desde" , "para" , "al" , "sin" , "se" , "con"]
#     palabras_claves = [palabra for palabra in texto.split() if palabra.lower() not in [palabra.lower() for palabra in lista]]
#     return palabras_claves

# def nivel_educativo (empresa , usuario:list):
#     lista = []
#     NIVELES_EDUCATIVOS = ["tecnico" , "tecnologo" , "ingeniero" , "licenciatura" , "master" , "doctorado"]
#     empresa_index = NIVELES_EDUCATIVOS.index(empresa.lower())
#     for i in range(len(usuario)):
#             x =usuario[i][0]
#             if x.lower() in NIVELES_EDUCATIVOS:
#                 educacion = usuario[i][0]
#                 usuario_index = NIVELES_EDUCATIVOS.index(educacion.lower())
#                 if usuario_index >= empresa_index:
#                     lista.append (usuario[i][1])
#     return lista


# def puntaje_ubicacion (distancia:str) :
#     puntajes = {
#         (0, 5): 10,
#         (6, 8): 9,
#         (9, 11): 8,
#         (12, 14): 7,
#         (15, 17): 6,
#         (18, 20): 5,
#         (21, 23): 3,
#         (24, None): 1,
#     }
#     for i in distancia.split():
#         if i == "m":
#             return 10
#         elif i == "km":
#             numero = distancia[:-3]
#     numero = float(numero)

#     for rango, puntaje in puntajes.items():
#         if rango[0] <= numero <= rango[1]:
#             return puntaje