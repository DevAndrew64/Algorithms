def quick_sort(arr):
    if len(arr) <= 1:
        return arr # Lista con 0 o 1 elementos ya esta organizada
    
    pivote = arr[len(arr) // 2]
    
    
    # Particionamos lista en 3 partes
    left = [x for x in arr if x < pivote]
    middle = [x for x in arr if x == pivote]
    right = [x for x in arr if x > pivote]
    
    # Aqui aplicaros quicksort recursivamente a las sublistas
    return quick_sort(left) + middle + quick_sort(right)

# Prueba del algoritmo
lista = [8, 4, 7, 3, 9, 2, 5]
print("Lista ordenada:", quick_sort(lista))