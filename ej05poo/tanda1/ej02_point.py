"""
Implementamos una clase Punto (Point) con sus atributos x e y (estado). El comportamiento de la clase viene determinado
por su constructor (vacío y con dos parámetros), getters y setters (propiedades) y un método (invert_coordinates()) que
invierte las coordenadas x e y del punto, además la clase debe tener un __str__() para poder imprimir los puntos en
formato '(x,y)' y un __repr__() que nos devuelve la forma canónica del objeto.

Usamos el decorador @typechecked para evitar que se puedan pasar a los métodos parámetros de tipo incorrecto. Se puede
aplicar a la clase, y comprobará el tipo de todos los métodos anotados (salvo clases internas) o a los métodos de forma
individual.

Autor: Rafael del Castillo Gomariz.
Fecha: 15/1/2023.
"""
