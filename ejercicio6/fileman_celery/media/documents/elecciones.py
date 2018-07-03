'''
Diseñar y elaborar un programa que calcule y muestre las estadísticas por:
1) Votos para cada candidato
2) Votos por sexo para cada candidato
3) Votos por rango de edad para cada candidato:
    a) [18,25]
    b) [26,35]
    c) [36,45]
    d) 46 en adelante

4) Votos por región para cada candidato:
    a) Región Caribe
    b) Región Andina
    c) Eje Cafetero
    d) Región Pacifica
    e) Llanos Orientales

5) Mostrar los resultados Ordenados de Mayor a menor.
'''
from random import randint, choice

# Constantes para La base de datos
REGIONES = ['REGION CARIBE',
            'REGION ANDINA',
            'EJE CAFETERO',
            'REGION PACIFICA',
            'LLANOS ORIENTALES'
            ]
CANDIDATOS = ['PETROSKY', 'PORKY_DUQUE']

NAMES = ['Juan', 'Jose', 'Ana', 'Beatriz', 'Camila', 'Carmen', 'Delia', 'Dora',
         'Fredy' 'Mendoza', 'Vargas', 'Martinez', 'Garcia', 'Marquez', 'Isaac',
         'Monterroza', 'Daniel', 'Galarcio', 'Windy', 'Cantillo', 'Sierra'
         ]


class Votante:
    '''
    Entidad que describe el Votante
    '''

    def __init__(self, nombre='', edad=18, sexo='MASCULINO', region='REGION CARIBE', voto='PETROSKY'):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.region = region
        self.voto = voto

    def __str__(self):
        return 'Nombre: {}\nEdad: {}, Sexo: {}\nVotó: {}\n\n'.format(
            self.nombre, self.edad, self.sexo, self.voto)


def create_database(n_votantes=1000):
    '''
    Función que genera una Base de datos aleatoria de Votante
    :param n_votantes: Numero de votantes a generar (por defecto = 1000)
    :return: Una Lista de Votante -> [Votante]
    '''
    return [
        Votante(
            '{} {}'.format(choice(NAMES), choice(NAMES)),
            randint(18, 80),
            choice(['MASCULINO', 'FEMENINO']),
            choice(REGIONES),
            choice(CANDIDATOS)
        )
        for vot in range(n_votantes)
    ]


# Algoritmos de Ordenamientos
def burbuja_ordenar(datos, order='>'):
    for i in range(1, len(datos)):
        for j in range(0, len(datos) - i):
            op_bool = datos[j]['votos'] < datos[j + 1]['votos'] if (order == '>') \
                else datos[j]['votos'] > datos[j + 1]['votos']
            if (op_bool):
                k = datos[j + 1]
                datos[j + 1] = datos[j]
                datos[j] = k;


def selection_ordenar(datos, order='>'):
    for i in range(0, len(datos) - 1):
        point = i
        for j in range(i + 1, len(datos)):
            op_bool = datos[point]['votos'] < datos[j]['votos'] if order == '>' \
                else datos[point]['votos'] > datos[j]['votos']
            if op_bool:
                point = j
        k = datos[point]
        datos[point] = datos[i]
        datos[i] = k

def insercion_ordenar(datos):
    for i in range(1, len(datos)):
        init=datos[i]
        j=i-1
        while j >= 0 and datos[j]['votos'] < init['votos']:
            datos[j + 1] = datos[j]
            j=j-1
        datos[j + 1]=init

# Mis Funciones
def votos_candidatos(datos):
    num_x_cand = [{'label': x, 'votos': 0} for x in CANDIDATOS]
    for votante in datos:
        for cand in range(len(CANDIDATOS)):
            if votante.voto == CANDIDATOS[cand]:
                num_x_cand[cand]['votos'] += 1
                break
    return num_x_cand


def votos_sex_candidatos(datos, candidato):
    num_x_sexo = [
        {'label': 'MASCULINO', 'votos': 0},
        {'label': 'FEMENINO', 'votos': 0}
    ]
    for votante in datos:
        if votante.voto == candidato and votante.sexo == 'MASCULINO':
            num_x_sexo[0]['votos'] += 1
        elif votante.voto == candidato and votante.sexo == 'FEMENINO':
            num_x_sexo[1]['votos'] += 1

    return num_x_sexo


def votos_rango_edad_candidatos(datos, candidato, edades):
    votos_x_edad = [{'label': '{}->{}'.format(x[0], x[1]), 'votos': 0} for x in edades]
    for votante in datos:
        for index, edad in enumerate(edades):
            if (edad[1] != '++'):
                if votante.voto == candidato and votante.edad >= edad[0] and votante.edad <= edad[1]:
                    votos_x_edad[index]['votos'] += 1
                    break
            else:
                if votante.voto == candidato and votante.edad >= edad[0]:
                    votos_x_edad[index]['votos'] += 1
                    break
    return votos_x_edad


def votos_region_candidatos(datos, candidato):
    num_x_region = [{'label': x, 'votos': 0} for x in REGIONES]
    for votante in datos:
        for reg in range(len(REGIONES)):
            if votante.voto == candidato and votante.region == REGIONES[reg]:
                num_x_region[reg]['votos'] += 1
                break
    return num_x_region


if __name__ == '__main__':
    datos = create_database()
    rango_edades = [[18, 25], [26, 35], [36, 45], [46, '++']]
    print('******************* NUMERO DE VOTOS DE LOS CANDIDATOS ********************')
    print(votos_candidatos(datos))
    print('*********************************************************************\n\n')

    for candidato in CANDIDATOS:
        print('*********************************************************************')
        print('********* Detalle del candidato {} **************\n'.format(candidato))
        votos_sex = votos_sex_candidatos(datos, candidato)
        print(votos_sex)
        print('**********Ordenado********')
        # burbuja_ordenar(votos_sex)
        # selection_ordenar(votos_sex)
        insercion_ordenar(votos_sex)
        print(votos_sex)
        print('**********FIN-Ordenado********')
        votos_edad = votos_rango_edad_candidatos(datos, candidato, rango_edades)
        print(votos_edad)

        votos_region = votos_region_candidatos(datos, candidato)
        print(votos_region)
        print('*********************************************************************\n')
