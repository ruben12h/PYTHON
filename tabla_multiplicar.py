
# Este programa genera una tabla de multiplicar del 1 al 10.

def tabla_de_multiplicar():
    # Iteramos del 1 al 10 para la base de la tabla
    for i in range(1, 11):
        print(f"Tabla del {i}:")
        # Iteramos del 1 al 10 para el multiplicador
        for j in range(1, 11):
            # Imprimimos el resultado de la multiplicación
            print(f"{i} x {j} = {i * j}")
        # Añadimos una línea en blanco para separar las tablas
        print()

# Llamamos a la función para generar la tabla
tabla_de_multiplicar()
