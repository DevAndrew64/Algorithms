def heapify(arr, n, i):
    largest = i # Se asume que la raiz es el nodo mas grande
    left = 2 * i + 1 # Hijo izquierdo
    right = 2 * i + 2 # Hijo derecho
    
    # Si el hijo izquierdo es mayor que la raiz
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    # Si el hijo derecho es mayor que el mayor hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    # Si el mayor no es la raiz, intercambiamos y seguimos heapificando
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heap_sort(arr):
    n = len(arr)
    
    # Aqui construimos un Max-heap (Reorganizar e arreglo)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # Extraer los elementos uno por uno del heap
    for i in range(n - 1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # intercambio
        heapify(arr, i, 0) # Restaurar el heap
        
Lista = [90, 120, 20, 54, 32, 78, 12, 4, 1, 43]
heap_sort(Lista)
print("Lista ordenada: ", Lista)
    
    