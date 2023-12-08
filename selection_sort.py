from swap import swap

arr = [17, 6, 8, 26, 7]

def selection_sort(array, size):
    size= len(arr)
    for i in range(size):
        min_index = i
        for j in range(array):
            if array[j] < array[min_index]:
                min_index = j
        swap(arr)
        
selection_sort(arr)       
print(arr)