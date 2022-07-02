#Algoritmo Quicksort
import math
import numpy as np
import time
import sys

# Obtener el maximo limite de profundidad
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

"Alternativa #1: Cálculo del angulo de un vector cada vez que se accede a su valor"
#Particion realizada segun el esquema de Lomuto. Utiliza como pivot el ultimo elemento y al finalizar quedan a la izquierda del pivot 
#todos los valores menores que el y a la derecha los mayores.
#Devuele la posicion que ocupa el pivote al final
def particion1(A,lo,hi,vector):
    pivot = calcAngl(A[hi],vector)  #El pivot sera el ultimo elemento    
    i = lo-1                        #Indice del pivot

    for j in range(lo, hi):
        #Si el elemento actual is menor o igual que el del pivote, movemos el indice el pivote hacia adelante
        if calcAngl(A[j],vector) <= pivot:
            i += 1
             #Intercambiar el elemento actual con el elemento en el pivote
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
            
    #Movemos el pivote de tal manera que, los elementos que estén a la izquierda serán menores y los de la derecha serán mayores
    ux = A[i+1]
    A[i+1] = A[hi]
    A[hi] = ux

    return i+1

def quicksort1(A, lo, hi,vector):
    if lo >= 0 and hi >= 0 and lo < hi:
        p = particion1(A,lo,hi,vector)

        #Ordenamos las 2 partes
        quicksort1(A,lo,p-1,vector) #Parte izquierda del pivote
        quicksort1(A,p+1,hi,vector) #Parte derecha del pivote

#*******************************************************************************************************************************************

"Aternativa #2: Cálculo del angulo antes de ordenar los vectores del array"
#Particion realizada segun el esquema de Lomuto. Utiliza como pivot el ultimo elemento y al finalizar quedan a la izquierda del pivot 
#todos los valores menores que el y a la derecha los mayores.
#Devuele la posicion que ocupa el pivote al final
def particion2(A,lo,hi):
    pivot = A[hi][2]  #El pivot sera el ultimo elemento
    i = lo -1         #Indice del pivot

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

def quicksort2(A, lo, hi):
    if lo >= 0 and hi >= 0 and lo < hi:
        p = particion2(A,lo,hi)

        #Ordenamos las 2 partes
        quicksort2(A,lo,p-1) #Parte izquierda del pivote
        quicksort2(A,p+1,hi) #Parte derecha del pivote

#Main
vector = (1,1)
n = 10000
for i in range(5):
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
        array1 = list(array1)

    if (0,0) in array2:
        array2 = list(np.where(array2 == (0,0), (1,1), array2))
    else:
        array2 = list(array2)

    #Hacer solo para la alternativa #2
    "Angulos calculados antes de llamar al algoritmo"
    j = 0
    for item in array2:
        item = np.append(item,calcAngl(item,vector))
        array2[j] = item
        j += 1
       
    t0 = time.time()
    quicksort1(array1,0,len(array1)-1,vector) #Alternativa #1
    t1 = time.time()
    quicksort2(array2,0,len(array2)-1) #Alternativa #2
    t2 = time.time()

    print("{}-{}   -   {}".format("#1.Tamaño de n:",n,t1-t0))
    print("{}-{}   -   {}".format("#2.Tamaño de n:",n,t2-t1))

    array1.clear()
    array2.clear()

    n *= 2
