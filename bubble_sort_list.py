#last element will be sorted first
def bubble_sort(list):
    length = len(list)
    for i in range(length-1):
        for j in range(length - i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


list = [5, 4, 3, 7, 1, 6, 0]
bubble_sort(list)
print('sorted list :', list)