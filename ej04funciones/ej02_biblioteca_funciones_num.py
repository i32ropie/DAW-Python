"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro
de otras si es necesario.

Observa bien lo que hace cada función, ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo.
Por ejemplo, la función es_capicua() resulta trivial teniendo voltea() y la función siguiente_primo() también es muy
fácil de implementar teniendo es_primo().

Prohibido utilizar funciones de conversión del número a una cadena.

- es_capicua: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario
- es_primo: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario
- siguiente_primo: devuelve el menor primo que es mayor al número que se pasa como parámetro
- digitos: devuelve el número de dígitos de un número entero
- voltea: le da la vuelta a un número
- digito_n: devuelve el dígito que está en la posición n de un entero. Se empieza por 0 y de izquierda a derecha.
- posicion_de_digito: da la posición de la 1ª ocurrencia de un dígito dentro de un entero. Si no está, devuelve -1.
- quita_por_detras: le quita a un número n dígitos por detrás (por la derecha).
- quita_por_delante: le quita a un número n dígitos por delante (por la izquierda).
- pega_por_detras: añade un dígito a un número por detrás.
- pega_por_delante: añade un dígito a un número por delante.
- trozo_de_numero: toma como parámetros las posiciones inicial y final de un número y devuelve el trozo correspondiente.
- junta_numeros: pega dos números para formar uno.

En esta biblioteca se hace un test haciendo assert de las diferentes funciones. Además, las funciones lanzan la
excepción ValueError si se le pasan parámetros erróneos.

Autor: Rafael del Castillo Gomariz
Fecha: 8/12/2022
"""
