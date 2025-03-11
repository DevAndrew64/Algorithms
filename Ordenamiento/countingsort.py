def counting_sort(arr):
    if not arr:
        return []
    
    max_value = max(arr)
    count = [0] * (max_value + 1)
    
    # Contar ocurrencias por cada numero
    for num in arr:
        count[num] += 1
        
    # Se arma lista ordenada
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq) # Agregar el numero freq veces (frecuencia)
        
    return sorted_arr

# Prueba del algoritmo
lista = [4, 2, 2, 8, 3, 3, 1]
print("Lista ordenada:", counting_sort(lista))  # Salida: [1, 2, 2, 3, 3, 4, 8]