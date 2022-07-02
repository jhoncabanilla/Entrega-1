#Optimizacion de Quicksort recursivo. Metodo #2
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
#Particion realizada segun el esquema de Lomuto. Utiliza como pivot el ultimo elemento y al finalizar quedan a la izquierda del pivot 
#todos los valores menores que el y a la derecha los mayores.
#Devuele la posicion que ocupa el pivote al final
def particion_1(A,lo,hi):
    pivot = A[hi][2]    #El pivot sera el ultimo elemento
    i = lo -1           #Indice del pivot

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

def quicksort_Metodo2_1(A, lo, hi):
    while lo < hi:
        p = particion_1(A,lo,hi) #Posicion del pivote

        #Llamada recursiva de Quicksort para ordenar los elementos a la izquierda del pivote
        quicksort_Metodo2_1(A,lo,p-1)
        lo = p + 1

#*******************************************************************************************************************************************
"ALTERNATIVA #2"
def particion_2(A,lo,hi,vector):
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

def quicksort_Metodo2_2(A, lo, hi,vector):
    while lo < hi:
        p = particion_2(A,lo,hi,vector) #Posicion del pivote

        #Llamada recursiva de Quicksort para ordenar los elementos a la izquierda del pivote
        quicksort_Metodo2_2(A,lo,p-1,vector)
        lo = p + 1


#Main
vector = (1,1)
n = 10000

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
    for item in array1:
        item = np.append(item,calcAngl(item,vector))
        array1[j] = item
        j += 1
       
    t0 = time.time()
    quicksort_Metodo2_1(array1,0,len(array1)-1)  #ALTERNATIVA #2: CON PRECALCULO DE ANGULO 
    t1 = time.time()
    quicksort_Metodo2_2(array2,0,len(array1)-1,vector)#ALTERNATIVA #1: SIN PRECALCULO DE ANGULO
    t2 = time.time()

    print("{}-{}  -   {}".format("Quicksort (precalculo)",n,t1-t0))
    print("{}-{}  -   {}".format("Quicksort (sin precalculo)",n,t2-t1))

    #Vaciamos el array y procedemos a crear uno nuevo aleatorio
    array1.clear()
    array2.clear()
    n *= 2
