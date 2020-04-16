def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1

    return even, odd


lst = [20, 25, 12, 13, 45, 40, 98]
even, odd = count(lst)
print("even :", even, " odd :", odd)