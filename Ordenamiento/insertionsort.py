def insertion_sort(arr):
    for i in range(1, len(arr)): # Empezamos en el segundo elemento
        key = arr[i] # Guardamos el valor actual
        j = i - 1 # Empezamos comparando con el elemento anterior
        
        # Desplazamos los elementos mayores hacia la derecha
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key # Insertamos el elemento en su posición correcta
    return arr

# Prueba del algoritmo
lista = [5, 3, 8, 6, 2]
print("Lista ordenada:", insertion_sort(lista))