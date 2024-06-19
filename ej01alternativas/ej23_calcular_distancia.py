"""
Programa: ej23_calcular_distancia.py

Propósito: dados cinco números enteros, hay que determinar cuál de los cuatro últimos
números es más cercano al primero.
Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que
el número más cercano al 2 es el 1.

Autor: Rafael del Castillo.
Fecha: 4/11/2020.
-------------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------------
Calcularemos la distancia entre el primer y el segundo número, poniendo a éste último
como candidato a ser el más cercano.

Comprobaremos para el resto de los números su distancia con el primero, y si fuera menor que
la del candidato, lo sustituiremos.
--------------------------------------------------------------------------------------------
Algoritmo:
--------------------------------------------------------------------------------------------
Variables
- n1, n2, n3, n4 y n5:  los cinco números introducidos.
- distance: guardará la "distancia" del primer número con el candidato.
- candidate: número candidato a tener la menor distancia.

PEDIR n1,n2,n3,n4,n5
candidate <-- n2
distance <-- ABS(n1 - n2)

* Tercero número
SI ABS(n1 - n3) < distancia
    candidate <-- n3
    distance <-- ABS(n1 - n3)
FIN-SI

* Cuarto número
SI ABS(n1 - n4) < distancia
    candidate <-- n4
    distance <-- ABS(n1 - n4)
FIN-SI

* Quinto número
SI ABS(n1 - n5) < distancia
    candidate <-- n5
    distance <-- ABS(n1 - n5)
FIN-SI

* Muestro resultados
ESCRIBIR candidate
"""
