def selectionsort(arr):
    n = len(arr)
    for i in range(n - 1): # Recorrer lista completa
        min_indezx = i
        for j in range(i + 1, n): # Buscar el elemento minimo
            if arr[j] < arr[min_indezx]:
                min_indezx = j # Actualizar el indice minomo encontrado
                
        # Intercambiar el mínimo con el primer elemento de la parte desordenada
        arr[i], arr[min_indezx] = arr[min_indezx], arr[i]
        
Lista = [64, 34, 25, 12, 22, 11, 90]
print(selectionsort(Lista))