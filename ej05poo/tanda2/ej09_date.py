"""
Implementación de una clase Fecha (mutable).

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

Tendremos métodos para:

- Sumar y restar días a la fecha.
- Restar fechas. Devuelve el número de días comprendidos entre ambas.
- Comparar la fecha almacenada con otra.
- Saber si el año de la fecha almacenada es bisiesto.
- Obtener el día de la semana de una fecha concreta.
- El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".

Autor: Rafael del Castillo Gomariz.
"""
