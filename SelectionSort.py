from swap import swap

def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        swap(A, i, min_idx)
    return A

A = [17, 6, 8, 26, 9, 7]

print(selection_sort(A))