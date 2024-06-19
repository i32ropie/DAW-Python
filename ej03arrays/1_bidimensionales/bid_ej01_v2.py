"""
Programa que pide 20 números enteros.

Estos números se introducen en un array de 4 filas por 5 columnas.
El programa muestra las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total aparece en la esquina inferior derecha.

Ejercicio del libro "Aprende Java con Ejercicios edición 2018" (https://leanpub.com/aprendejava).

En esta versión mejoramos los siguientes aspectos:

- El ancho de visualización de cada número lo calculamos automáticamente (no es 3 como antes).
- A la hora de imprimir las casillas y calcular el sumatorio de las filas, contemplamos que un array bidimensional es
  un array de arrays de una dimensión y usamos la función sum().

@author Rafael del Castillo
"""
