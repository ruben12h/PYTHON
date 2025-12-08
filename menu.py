#hacer un menu de opciones que incluya la opcion de salir del pograma 

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n--- Menú de Opciones ---")
    print("1. Sumar")
    print("2. Multiplicar")
    print("3. Dividir")
    print("4. Salir")
    print("--------------------")

def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Ha seleccionado la opción de Sumar.")
            # Aquí iría la lógica para la suma
        elif opcion == '2':
            print("Ha seleccionado la opción de Multiplicar.")
            # Aquí iría la lógica para la multiplicación
        elif opcion == '3':
            print("Ha seleccionado la opción de Dividir.")
            # Aquí iría la lógica para la división
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
