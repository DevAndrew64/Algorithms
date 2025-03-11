def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index # Retorna la posicion (indice) del elemento encontrado
    return -1 # Si no se encuentra el elemento, devuelve -1

lista = [3, 4, 6, 1, 20, 41, 43, 80, 32, 41, 23, 53]
objetivo = 23
resultado = linear_search(lista, objetivo)

if resultado != 1:
    print(f"Elemento {objetivo} encontrado en la posicion {resultado}")
else:
    print(f"Elemento {objetivo} no encontrado en la lista")