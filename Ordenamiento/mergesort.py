def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
     # Combinar ambas mitades ordenadas
    return merge(left_half, right_half)
    
def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
            
        else:
            sorted_list.append(right[j])
            j += 1
            
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list


lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista ordenada:", merge_sort(lista))