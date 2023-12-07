my_list = [2, 1, 3, 8, 4]

def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1],my_list[j]

bubble_sort(my_list)
print("Sortierte Zahlen: ",my_list)