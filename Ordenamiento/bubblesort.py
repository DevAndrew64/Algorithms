def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break
        
    return arr
Lista = [64, 34, 25, 12, 22, 11, 90, 120, 50]
print(bubblesort(Lista))