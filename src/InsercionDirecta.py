"Algoritmo de Insercion Directa"

import math
import time
import numpy as np

"""
Funcion mediante la cual devuelvo el angulo que forman dos vectores cualquiera.
Para llevar a cabo algunas de estas operaciones(raiz cuadrada o pasar de radianes a grados) 
es necesario importar la libreria math
"""
def calcAngl(u,v):
    divid = u[0]*v[0] + u[1]*v[1]
    divis = (math.sqrt(pow(u[0],2)+pow(u[1],2))) * (math.sqrt(pow(v[0],2)+pow(v[1],2)))
    return math.degrees(math.acos(divid / divis))


"Alternativa #1: Cálculo del angulo de un vector cada vez que se accede a su valor"
def OrdenacionInsercion_1(v,vector):
    i = 1
    while i < len(v):
        x = v[i]
        x2 = calcAngl(x, vector)   #Angulo entre los vectores del array y el vector dado
        j = i - 1
        while j >= 0 and calcAngl(v[j],vector) > x2:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x
        i += 1


#***************************************************************************************************************
"Alternativa #2: Cálculo del angulo antes de ordenar los vectores del array"
def OrdenacionInsercion_2(v):
    i = 1
    while i < len(v):
        x = v[i][2]     #Accedo a la posicion indicada ya que ahí guardo el angulo que forman v[i] con el vector dado
        aux = v[i]
        j = i - 1
        while j >= 0 and  v[j][2]> x:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = aux
        i += 1


#Main
vector = (1,1)

#Tiempo de ejecucion
n = 1000
for i in range(3):
    #Para crear arrays de vectores aleatorios utilizo los arrays numpy.
    #En este caso mediante el metodo .random.randint(x,y,(n,2)), creo vectores bidimensionales comprendidos entre -10 y 100
    #El array creado tendrá longitud n

    array1 = np.random.randint(-10,100,(n,2))
    array2 = np.random.randint(-10,100,(n,2))

    #Una vez creados los arrays compruebo que no haya vectores (0,0).
    #Si encuentra alguno, simplemente los sustituyo por el vector (1,1) mediante el metodo .where de numpy
    if (0,0) in array1:
        array1 = list(np.where(array1 == (0,0), (1,1), array1))
    else:
        array1= list(array1)

    if (0,0) in array2:
        array2 = list(np.where(array2 == (0,0), (1,1), array2))
    else:
        array2 = list(array2)

     #Hacer solo para la alternativa #2
    #Calculo los angulo antes de ordenar los vectores
    #Para ello, por cada item del array, lo que hago es añadir una tercera coordenada a los vectores que sera el angulo que formen con el vector dado
    j = 0
    for item in array2:
        item = np.append(item,calcAngl(item,vector))
        array2[j] = item
        j += 1

    #Para las mediciones de los tiempos utilizo time()
    t0 = time.time()
    OrdenacionInsercion_1(array1,vector)
    t1 = time.time()
    OrdenacionInsercion_2(array2)
    t2 = time.time()

    print("{} {}  -   {}".format("Insercion directa(#1):",n,t1-t0))
    print("{} {}  -   {}".format("Insercion directa(#2):",n,t2-t1))

    #Hago este clear para vaciar por completo los arrays, debido a que al añadir los angulos en una iteracion que no fuese la primera me daba error, ya que se guardaban
    #hasta 3,4 o 5 angulos en cada vector
    array1.clear()
    array2.clear()
    n *= 2