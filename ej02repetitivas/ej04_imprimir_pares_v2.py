"""
Escribir un programa que imprima todos los números pares entre dos números que
se le pidan al usuario.

Versión con ciclo for.

Análisis
--------
Leemos un número. Si es impar, le sumo 1 y ya es par. Leemos el segundo número.
Escribo el número desde el primero hasta el segundo de dos en dos.
Datos de entrada: dos números.
Información de salida: Los números pares que hay entre los dos anteriores.
Variables: num,num1,num2 (entero).

Diseño
------
1.- Leer num1,num2
2.- Si num1 es mayor que num2 intercambio el valor de las variables
3.- Si num1 es impar -> num1=num1+1
4.- Desde num1 hasta num2 de 2 en 2
5.- Escribir el número
"""

print("Pares comprendidos entre dos números")
print("------------------------------------")

# Pedimos datos
num1 = int(input("Introduce el número 1: "))
num2 = int(input("Introduce el número 2: "))

# ¿Intercambiamos?
if num1 > num2:
    num1, num2 = num2, num1  # solo en Python

# Si primer número es impar pasamos al siguiente par
if num1 % 2 == 1:
    num1 += 1

# Mostramos salida
for num in range(num1, num2 + 1, 2):
    print(f"{num} ", end="")
