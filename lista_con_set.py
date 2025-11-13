
# Este programa demuestra cómo usar un set para eliminar duplicados de una lista.

# 1. Creamos una lista con elementos duplicados.
lista_original = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7]

print(f"Lista Original: {lista_original}")
print(f"Longitud de la Lista Original: {len(lista_original)}")
print("-" * 30)

# 2. Convertimos la lista a un set para eliminar los duplicados.
# Un set es una colección de elementos únicos y desordenados.
set_de_lista = set(lista_original)

print(f"Set creado desde la lista: {set_de_lista}")
print(f"Longitud del Set: {len(set_de_lista)}")
print("-" * 30)

# 3. Convertimos el set de nuevo a una lista (si es necesario).
# El orden de los elementos no está garantizado.
lista_sin_duplicados = list(set_de_lista)

print(f"Lista Final (sin duplicados): {lista_sin_duplicados}")
print(f"Longitud de la Lista Final: {len(lista_sin_duplicados)}")

