"""
Propósito: Calcular la potencia. Pedimos una base (real) y un exponente (entero positivo).
No usamos el operador de potencia ni la función.

Autor: Rafael del Castillo.
Fecha: 11/11/2020.
---------------------------------------------------------------------------------------------------------------
Análisis:
---------------------------------------------------------------------------------------------------------------
El resultado de elevar una base a un exponente entero es:

- Si el exponente es 0 es 1.
- Si el exponente es positivo, la base multiplicada por si misma tantas veces como el valor del exponente.
- Si el exponente es negativo, el inverso de la base elevada al valor absoluto del exponente.

Podemos calcular la potencia con el valor absoluto del exponente y si este es negativo calcular el inverso del
resultado anterior.
---------------------------------------------------------------------------------------------------------------
Algoritmo:
---------------------------------------------------------------------------------------------------------------
Variables:

- potencia: real, guardaremos el valor de la potencia, inicializamos a 1
- base: real.
- exponente: entero

potencia <-- 1
PEDIR base, exponente

PARA i DESDE 1 HASTA ABS(exponente)
    potencia <-- potencia * base
FIN-PARA

SI exponente < 0
    potencia <-- 1/potencia
FIN-SI

ESCRIBIR potencia
---------------------------------------------------------------------------------------------------------------
"""
