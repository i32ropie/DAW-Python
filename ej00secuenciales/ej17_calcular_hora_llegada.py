"""
Programa ej17_calcular_hora_llegada.py

Propósito: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El time de viaje hasta llegar a otra ciudad B es de T segundos.
Se pide determinar la hora de llegada a la ciudad B.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Tenemos que pedir la hora de salida (hora, minutos y segundos).
Tenemos que saber también el time en segundos que ha tardado en llegar.
Tenemos que calcular la hora de llegada.

Datos de entrada: hora, minutos y segundos de salida (enteros), segundos que tarda (entero).
Información de salida: hora, minutos y segundos de llegada (enteros).

Variables:  departure_hour, departure_minute, departure_second, travel_seconds,
            arrival_hour, arrival_minute, arrival_second (enteros)

------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer hora de salida
2. Leer segundos que tarda
3. Convierto la hora de salida a segundos (necesito una variable departure_time_in_seconds)
4. Le sumo los segundos que he tardado (necesito una variable arrival_time_in_seconds)
5. Convierto los segundos totales a hora, minuto y segundos
6. Muestro la hora de llegada
"""
