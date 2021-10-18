"""
Aplicación que permita adivinar un número.

La aplicación genera un número aleatorio del 1 al 100. A continuación va
pidiendo números y va respondiendo si el número a adivinar es mayor o
menor que el introducido, además de los intentos que te quedan
(tienes 10 intentos para acertarlo).

El programa termina cuando se acierta el número (además te dice en
cuantos intentos lo has acertado), si se llega al limite de intentos te
muestra el número que había generado.

Fecha: 11/11/2019.

Autores: Clase de 1ºDAW

Otra versión del programa anterior.
"""

import random

# Constantes
INTENTOS_MAXIMOS = 10

# Inicializamos
numero_a_adivinar = random.randint(1, 100)

# Proceso

# implementamos un ciclo postcondición, ejecutamos la instrucción
# antes de entrar en el ciclo y al final del ciclo.
numero_introducido = int(input("Introduce un número entre 1 y 100: "))
intentos_que_quedan = INTENTOS_MAXIMOS - 1
while numero_introducido != numero_a_adivinar and intentos_que_quedan > 0:
    if numero_introducido < numero_a_adivinar:
        print(f"{numero_introducido} es menor que el número a adivinar.")
    else:
        print(f"{numero_introducido} es mayor que el número a adivinar.")
    numero_introducido = int(input("Te quedan " + str(intentos_que_quedan) +
                                   " intentos. Introduce un número entre 1 y 100: "))
    intentos_que_quedan -= 1

# Mostramos resultado
if numero_introducido == numero_a_adivinar:  # ha adivinado
    print(f"Has adivinado el número en {INTENTOS_MAXIMOS - intentos_que_quedan} intentos")
else:
    print(f"Has agotado el número máximo de intentos. El número a adivinar era {numero_a_adivinar}")
