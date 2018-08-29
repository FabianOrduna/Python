# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:46:46 2018

@author: FORDUNAF

TAREA 1

Entregables: el texto de los programas en archivos .py, y, donde aplique, los archivos de datos requeridos.

Aunque en algunos casos no se mencione explícitamente, los programas deben ser modulares, segmentando los procesos
con funciones. Los programas deben tener comentarios adecuados (los cuales se calificarán).

Fecha de entrega: viernes 31-ago-2018

7.	Elabora los siguientes programas en Python.

a)	Un programa para hacer la multiplicación de dos matrices A(m, n) y B(n, p). Los datos pueden especificarse
explícitamente dentro del programa o ser leídos desde archivo.

b)	Un programa que lea los datos de dos polinomios, desde archivo, como se explica posteriormente, y que efectúe
las operaciones de suma y multiplicación de los polinomios. Los datos que el usuario proporcionará son los coeficientes
(reales) y los exponentes (enteros, >=0 y <=15) de ambos polinomios, los cuales pueden o no estar ordenados. El final de
cada polinomio está dado por un –1 como coeficiente y como exponente.

Los términos del polinomio resultante deberán ser desplegados en orden descendente, observando el siguiente formato:

± cX ^e

Donde:

± representa el signo del término

c representa el coeficiente del término

^ significa exponenciación

e representa el valor del exponente

Por ejemplo, supongamos que los datos son:

2.5 3 -4 2 6.5 1 3 4 -1 -1

-2 2 -3 4 9.1 1 6.9 8 -1 -1

Entonces, los polinomios que se van a operar son:
+2.5X3 - 4X2 + 6.5X1 + 3X4
-2X2 - 3X4 + 9.1X1 + 6.9X8
De tal forma que el resultado de la suma es:
6.9X8 + 2.5X3 - 6X2 + 15.6X1
y se desplegaría como:

+	6.9X^8 + 2.5X^3 - 6X^2 + 15.6X^1

c)	Un programa que contenga una función que reciba dos cadenas de caracteres, cuente y regrese la cantidad de veces que
    aparece la segunda cadena en la primera. Por ejemplo, si la primera cadena es 'azcbobobegghakl' y la segunda ´bob´,
    entonces la función regresará un dos.

El programa deberá imprimir:

Cantidad de veces que bob ocurre es: 2

d)	Un programa que lea palabras desde un archivo de texto y cuente cuántas veces aparece cada palabra distinta. Utiliza
    un diccionario para resolver el problema. También imprime la cantidad total de palabras distintas.

e)	Un programa que contenga una función que reciba un diccionario y regrese la cantidad de valores que contiene. Considera
    que los valores pueden ser de cualquier tipo (enteros, cadenas, listas, etc.). Prueba tu programa con diferentes tipos
    de valores.

f)	Un programa que inicialmente lea desde teclado dos cadenas (de 7 caracteres máximo) las cuales definirán un rango, por lo
    que la 1ª cadena deberá ser lexicográficamente menor que la 2ª. El programa leerá después n líneas desde un archivo de
    texto (cada línea de una longitud máxima de 40 caracteres).

Los primeros siete caracteres de cada línea del archivo de texto constituirán la "clave" de la misma. El programa leerá una
línea y si su clave está en el rango dado inicialmente, la escribirá en un archivo de salida. Por ejemplo, si el rango dado
es "Jaso" a "Ramos", entonces el archivo de salida contendrá todas aquellas líneas cuya clave lexicográficamente esté entre
estas dos cadenas.

Nota: no acentúes las palabras.
"""
def productoPunto(lista1, lista2):
    res = 0
    for g in range(0, len(lista1)):
        res+=lista1[g]*lista2[g] 
    return res

def multiplicaMatrices(A,B,m,n,p):
    #relleno la matriz de ceros
    ceros = [0 for j in range(0,m)]
    M = []
    for w in range(0,p):
        M.append(ceros)
        
        
    for x in range(0,m):
        for y in range(0,p):
            lista1 = []
            lista2 = []
            for h in range(0,n):
                if type(A[x]) == int:
                    lista1.append(A[x])
                else:
                    lista1.append(A[x][h])
                if type(B[x]) == int:
                    lista2.append(B[y])
                else:
                    lista2.append(B[y][h])
            #con lista1 la fila(horizontal) y lista2 la columna(vertical)
            M[y][x] = productoPunto(lista1, lista2)
    return M

def imprimeMatriz(M, m, n):
    #metodo que imprime matriz de m x n
    for j in range(0,m):
        for i in range(0,n):
            if i == 0:
                if type(M[i])!=int:
                    print(M[i][j] ," - ", end=""  )
                else:
                    print(M[i] ," - ", end=""  )
            elif i == n-1:
                if type(M[i])!=int:
                    print(M[i][j])
                else:
                    print(M[i])
            else:
                if type(M[i])!=int:
                    print(M[i][j], "- ", end="" )
                else:
                    print(M[i], "- ", end="" )
        
    return
A = [1,2,3]

B = [[1,15,0],[2,27,200]]

m = 1
n = len(A)
p = len(B)

M = multiplicaMatrices(A,B,m,n,p)

imprimeMatriz(M,m,p)
print(" ")
imprimeMatriz(B,3,2)
