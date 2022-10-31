################################################################################
# La política de cobro de una compañía telefónica es: cuando se realiza una
# llamada, el cobro es por el tiempo que esta dura, de tal forma que los primeros
# cinco minutos cuestan 1 euro por minuto, los siguientes tres, 80 céntimos,
# los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
# de mañana, 15 %, y en turno de tarde, 10 %.
# Haga un algoritmo para determinar cuánto debe pagar por cada concepto
# una persona que realiza una llamada.
################################################################################
# Análisis
# El precio final de la llamada depende del tiempo de la llamada.
# Los primeros cinco minutos cuestan 1 euro por minuto.
# Los siguientes 3 minutos, 80 céntimos.
# Los siguientes 2 minutos, 70 céntimos.
# A partir del minuto 10, 50 céntimos.
# Además, el coste depende del día u del turno, de esta manera:
# Si la llamada es el domingo, se suma el 3% al precio final
# Si la llamada es cualquier otro día por la mañana, se suma el 15% al precio final
# Si la llamada es cualquier otro día por la tarde, se suma el 10% al precio final
# Datos de entrada: tiempo de la llamada (entero),
# si la llamada es en domingo (carácter), turno (carácter)
# Información de salida: Precio de la llamada en euros (real)
# Variables: tiempo (entero), esDomingo, turno (carácter), coste (entero)
################################################################################
# Diseño
# 1. Leer tiempo
# 2. Leer si la llamada es en domingo
# 3. Si no es en domingo, leer el turno (Mañana o Tarde)
# 4. Si tiempo <5 coste=tiempo*100
# 5. Si tiempo<8 coste=(tiempo-5)*80 + 500 (el coste de los cinco primeros minutos)
# 6. Si tiempo<10 coste=(tiempo-8)*70 + 240 (el coste desde el minuto 6 al 8) + 500
# (el coste de los cinco primeros minutos)
# 7. Si tiempo>10 coste=(tiempo-10)*50 + 140 (el coste desde el minuto 9 al 10) + 240
# (el coste desde el minuto 6 al 8) + 500 (el coste de los cinco primeros minutos)
# 8. Si la llamada es en domingo coste = coste + 3%
# 9. Si la llamada es otro día por la mañana coste = coste + 15%
# 10. Si la llamada es otro día por la mañana coste = coste + 10%
# 11. Mostrar coste final en euros
################################################################################

# Pedimos datos
duration = int(input("¿Cuánto minutos dura la la llamada?: "))
is_sunday = input("¿Es Domingo? (S/N): ").upper()
if is_sunday == "N":
    turn = input("¿Qué turno: Mañana o Tarde? (M/T)?: ").upper()

# Proceso
if duration <= 5:
    cost = duration * 100
elif duration <= 8:
    cost = (duration - 5) * 80 + 500
elif duration <= 10:
    cost = (duration - 8) * 70 + 240 + 500
else:
    cost = (duration - 10) * 50 + 140 + 240 + 500

# impuestos
if is_sunday == "S":
    cost += cost * 0.03
elif turn == "M":
    cost += cost * 0.15
else:
    cost += cost * 0.10

# Salida
print("El coste de la llamada:", cost / 100, "euros.")
