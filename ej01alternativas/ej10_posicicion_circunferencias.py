"""
Programa que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
circunferencias y las clasifique en uno de estos estados:
exteriores
tangentes exteriores
secantes
tangentes interiores
interiores
concéntricas

Análisis
--------
Pedimos el centro (x1,y1) de una circunferencia y su radio r1, pedimos el
centro de otra circunferencia (x2,y2) y su radio r2.

En la siguiente página podemos aprender la relación entre dos circunferencias.
http://mimosa.pntic.mec.es/clobo/geoweb/circun3.htm

Datos de entrada: x1,y1,x3,y2,r1,r2 (real)
Información de salida: Tipo de relación entre las circunferencias
Variables: x1,y1,x3,y2,r1,r2 (real), distancia (real)

Diseño
------
1. Leer x1,y1,r1
2. Leer x2,y2,r2
3. Calcular distancia entre los centros
4. Si distancia>suma de los radios mostrar "Circunferencias exteriores"
5. Si distancia = suma de los radios mostrar "Tangentes exteriores"
6. Si distancia < suma de los radios Y distancia> que el valor absoluto de la
resta de los radios mostrar "Circunferencias secante"
7. Si distancia = que el valor absoluto de la resta de los radios mostrar
"Circunferencias tangentes interiores"
8. Si distancia >0 y distancia < que el valor absoluto de la resta de los
radios mostrar "Circunferencias interiores"
9. Si distancia = 0 mostrar "Circunferencias concéntricas"
"""

