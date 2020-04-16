#values must be sorted before applying this algorithm

pos = -1

def search(list, n):
    lower_bound = 0
    upper_bound = len(list)-1
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound)//2
        if list[mid] == n:
            global pos
            pos = mid+1
            print('found at :', pos)
            return True
        else:
            if  list[mid] < n:
                lower_bound = mid
            else:
                upper_bound = mid
    return False


list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3

if search(list, n):
    pass
else:
    print('not found')