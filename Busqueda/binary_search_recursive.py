def binary_search_recurisve(arr, target, left, right):
    if left > right:
        return -1 # No encontrado
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recurisve(arr, target, mid + 1, right)
    else:
        return binary_search_recurisve(arr, target, left, mid - 1)
    
Lista = [23, 2, 12, 43, 54, 76, 82, 90, 45, 18]
Objetivo = 90
Resultado = binary_search_recurisve(Lista, Objetivo, 0, len(Lista)-1)

if Resultado != -1:
    print(f"Se ha encontrado el objetivo {Objetivo} en el indice {Resultado}")
else:
    print(f"No se ha encontrado ninguna coincidencia para el objetivo {Objetivo}")