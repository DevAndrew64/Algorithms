def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2 # Se saca indice central entre izquierda y derecha
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1 # Buscar en la mitad izquierda
        else:
            right = mid - 1 # Buscar en la mitad derecha
            
    return -1

Lista = [23, 2, 12, 43, 54, 76, 82, 90, 45, 18]
Objetivo = 54
resultado = binary_search(Lista, Objetivo)

if resultado != -1:
    print(f"Se ha encontrado el objetivo {Objetivo} en el indice {resultado}")
else:
    print(f"No se ha encontrado ninguna coincidencia del objetivo {Objetivo}")