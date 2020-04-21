def selection_sort(list):
    length = len(list)
    for i in range(length-1):
        minpos = i
        for j in range(i, length):
            if list[j] < list[minpos]:
                minpos = j
        list[i], list[minpos] = list[minpos], list[i]

list = [10, 5, 43, 23, 1, 0, 78]
selection_sort(list)
print('sorted list :', list)