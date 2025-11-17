# -*- coding: utf-8 -*-
"""
Este archivo define una función para multiplicar dos números y muestra un ejemplo de su uso.
"""

def multiplicar(a, b):
    """
    Esta función toma dos números como entrada y devuelve su producto.

    Args:
        a (int or float): El primer número.
        b (int or float): El segundo número.

    Returns:
        int or float: El resultado de la multiplicación.
    """
    return a * b

# Ejemplo de uso de la función
if __name__ == "__main__":
    numero1 = 7
    numero2 = 6
    resultado = multiplicar(numero1, numero2)
    print(f"El resultado de multiplicar {numero1} por {numero2} es: {resultado}")

    # Otro ejemplo con números de punto flotante
    numero3 = 12.5
    numero4 = 2
    resultado2 = multiplicar(numero3, numero4)
    print(f"El resultado de multiplicar {numero3} por {numero4} es: {resultado2}")
