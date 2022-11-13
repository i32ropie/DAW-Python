"""
Cálculo del combinatorio de dos números.

Combinatorio(n,m) = n! / (m! * (n-m)!) si n>m
"""

# Inicializamos variables (acumuladores)
n_factorial = 1
m_factorial = 1
n_menos_m_factorial = 1

# Pedimos los datos: n y m de forma que n > m
while True:
    n = int(input("indique el valor de n (recuerde que debe ser mayor que m) "))
    m = int(input("indique el valor de m (recuerde que debe ser menor que n) "))
    if n > m:
        break

# Cálculo de n!
for i in range(n, 1, -1):  # va desde n hasta 2
    n_factorial = n_factorial * i  # nFactorial *= i

# Cálculo de m!
for i in range(m, 1, -1):
    m_factorial = m_factorial * i

# Cálculo de(n - m)!
for i in range(n - m, 1, -1):
    n_menos_m_factorial = n_menos_m_factorial * i

# Resultado
combinatorio = n_factorial // (m_factorial * n_menos_m_factorial)
print(f"El número combinatorio de {n} sobre {m} es {combinatorio}")
