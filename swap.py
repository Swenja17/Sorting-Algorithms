def swap (to_swap, a, b):
    to_swap[a], to_swap[b] = to_swap[b], to_swap[a]
    return to_swap


print(swap([1, 2, 3, 4, 5], 1, 3))
