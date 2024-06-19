"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
números a introducir). El programa debe informar de cuantos números introducidos
son mayores que 0, menores que 0 e iguales a 0.
---
Análisis
Se pide la cantidad de números que se van a leer. Vamos introduciendo números.
Tenemos que contar los positivos, negativos y 0.
Datos de entrada:Cantidad de números, los números.
Información de salida: Cantidad de positivos, de negativos y de 0.
Variables: cantidad_num, num, cont_positivos, cont_negativos, cont_ceros (enteros)
---
Diseño
1.- Inicializo los contadores
2.- Leer cantidad de números
3.- Desde 1 hasta cantidad de números
        Leer num
        Si num > 0-> incremento cont_positivos
        Si num < 0-> incremento cont_negativos
        Si num = 0-> incremento cont_ceros.
4.- Muestro contadores
"""
