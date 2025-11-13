
# Este programa le pide al usuario un número y genera su tabla de multiplicar.

def tabla_de_multiplicar_input():
    try:
        # Pedimos al usuario que introduzca un número entero
        numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
        
        print(f"Tabla del {numero}:")
        # Iteramos del 1 al 10 para el multiplicador
        for i in range(1, 11):
            # Imprimimos el resultado de la multiplicación
            print(f"{numero} x {i} = {numero * i}")
            
    except ValueError:
        # Manejamos el caso en que el usuario no introduce un número válido
        print("Error: Por favor, introduce un número entero válido.")

# Llamamos a la función para que se ejecute
tabla_de_multiplicar_input()
