"""
Clase que almacena duraciones de tiempo. Los objetos de esta clase son intervalos de tiempo y se crean de la forma:

- t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.
- t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.
- t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Tiene getters y setters mediante propiedades y métodos para:

- Sumar y restar objetos de la clase (el resultado es otro objeto).
- Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
- Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea '10h 35m 5s'

Aunque el ejercicio no lo pide, hemos implementado también la posibilidad de aplicar operaciones relacionales sobre
los objetos de esta clase sobrecargando los métodos correspondientes.

Autor: Rafael del Castillo Gomariz
"""
