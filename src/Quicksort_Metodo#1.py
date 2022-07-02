#Algoritmo Quicksort + Insertion Sort. Metodo #1
import math
import numpy as np
import time
import sys

# Obtener el maximo limite de profundid
sys.setrecursionlimit(6000)

"""
Funcion mediante la cual devuelvo el angulo que forman dos vectores cualquiera.
Para llevar a cabo algunas de estas operaciones(raiz cuadrada o pasar de radianes a grados) 
es necesario importar la libreria math
"""
def calcAngl(u,v):
    divid = u[0]*v[0] + u[1]*v[1]
    divis = (math.sqrt(pow(u[0],2)+pow(u[1],2))) * (math.sqrt(pow(v[0],2)+pow(v[1],2)))
    return math.degrees(math.acos(divid / divis))


"ALTERNATIVA #1: SIN PRECALCULO DE ANGULO"
def OrdenacionInsercion_1(v,lo,hi,vector):    
    for i in range(lo+1,hi+1):
        x = v[i] #Angulo de cada vector del array
        x2 = calcAngl(x,vector)
        j = i - 1
        while j >= lo and calcAngl(v[j],vector)> x2:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x

def particion_1(A,lo,hi,vector):
    pivot = calcAngl(A[hi],vector)  #El pivot sera el ultimo elemento
    i = lo -1   #Indice del pivot

    for j in range(lo, hi):
        #Si el elemento actual is menor o igual que el del pivote, movemos el indice el pivote hacia adelante
        if calcAngl(A[j],vector) <= pivot:
            i += 1
            #Intercambiar el elemento actual con el elemento en el pivote
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
    
    ux = A[i+1]
    A[i+1] = A[hi]
    A[hi] = ux

    return i+1

def quicksort_C_alter1(A,lo,hi,c,vector):
    while lo >= 0 and hi >= 0 and lo < hi:
        #Comprobar si la longitud del array es mayor a la constante c
        if hi-lo +1 > c:
            p = particion_1(A,lo,hi,vector) #Posicion del pivote

            #Procedemos a comprobar qué parte del array es más pequeña tras la partición, para así ordenar 
            #recursivamente esa parte y tratar la otra parte de forma iterativa.
            if p-lo < hi-p:
                quicksort_C_alter1(A,lo,p-1,c,vector) #Parte izquierda del pivote
                lo  = p + 1
            else:
                quicksort_C_alter1(A,p+1,hi,c,vector) #Parte derecha del pivote
                hi = p - 1
        else:
            OrdenacionInsercion_1(A,lo,hi,vector)
            break

#***********************************************************************************************************************************

"ALTERNATIVA #2: CON PRECALCULO DE ANGULO"
def OrdenacionInsercion_2(v,lo,hi):    
    for i in range(lo+1,hi+1):
        x = v[i][2] #Angulo de cada vector del array
        aux = v[i]
        j = i - 1
        while j >= lo and  v[j][2]> x:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = aux


def particion_2(A,lo,hi):
    pivot = A[hi][2]  #El pivot sera el ultimo elemento
    i = lo -1   #Indice del pivot

    for j in range(lo, hi):
        #Si el elemento actual is menor o igual que el del pivote, movemos el indice el pivote hacia adelante
        if A[j][2] <= pivot:
            i += 1
            #Intercambiar el elemento actual con el elemento en el pivote
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
    
    ux = A[i+1]
    A[i+1] = A[hi]
    A[hi] = ux

    return i+1


def quicksort_C_alter2(A,lo,hi,c):
    while lo >= 0 and hi >= 0 and lo < hi:
        #Comprobar si la longitud del array es mayor a la constante c
        if hi-lo +1 > c:
            p = particion_2(A,lo,hi)

            #Procedemos a comprobar qué parte del array es más pequeña tras la partición, para así ordenar 
            #recursivamente esa parte y tratar la otra parte de forma iterativa.
            if p-lo < hi-p:
                quicksort_C_alter2(A,lo,p-1,c) #Parte izquierda del pivote
                lo  = p + 1
            else:
                quicksort_C_alter2(A,p+1,hi,c) #Parte derecha del pivote
                hi = p - 1
        else:
            OrdenacionInsercion_2(A,lo,hi)
            break

#Main
vector = (1,1)
n = 10000
c = 50

#Tiempos de ejecucion
for i in range(4):
    array1 = np.random.randint(-10,100,(n,2))
    array2 = np.random.randint(-10,100,(n,2))

    #Una vez creados los arrays compruebo que no haya vectores (0,0).
    #Si encuentra alguno, simplemente los sustituyo por el vector (1,1) mediante el metodo .where de numpy   
    if (0,0) in array1:
        array1 = list(np.where(array1 == (0,0), (1,1), array1))
    else:
        array1 = list(array1)

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
       
    t0 = time.time()
    quicksort_C_alter1(array1,0,len(array1)-1,c,vector) #ALTERNATIVA #1: SIN PRECALCULO DE ANGULO"
    t1 = time.time()
    quicksort_C_alter2(array2,0,len(array2)-1,c) #ALTERNATIVA #2: CON PRECALCULO DE ANGULO"
    t2 = time.time()
    print("{}{}   -  {}{}  -   {}".format("Quicksort (sin precalculo) con limite:",c,"n:",n,t1-t0))
    print("{}{}   -  {}{}  -   {}".format("Quicksort (precalculo) con limite:",c,"n:",n,t2-t1))

    array1.clear()
    array2.clear()

    n *= 2