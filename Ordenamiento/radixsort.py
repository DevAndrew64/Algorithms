def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10 # Solo hay 10 digitos, 0-9
    
    # Contar ocurrencias del digito correspondiente
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    
    # Transformar count[i] para que contenga la posicion final del digito output
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    # Construir output array ordenado
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
        
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr) # Encuentra el numero mas grande
    exp = 1 # Empezar por las unidades
    
    while max_value // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10 # Pasar a la siguiente posicion decimal
        
Lista = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(Lista)
print("Lista ordenada Radix: ")  # [2, 24, 45, 66...