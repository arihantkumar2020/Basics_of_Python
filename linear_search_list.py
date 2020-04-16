pos = -1

def search(list, n):
    i = 0
    while i<len(list):
        if list[i] == n:
            global pos
            pos = i+1
            print('found at :', pos)
            return True
        i = i+1
    return False

list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 4

if search(list, n):
    pass
else:
    print('not found')