for i in range(0, 4):
    ascii1 = 65
    ascii2 = 79
    for j in range(0, 4):
        if j>i :
            print(chr(ascii2), end=' ')
            ascii2+=1
            ascii1+=1
        else:
            print(chr(ascii1), end=' ')
            ascii2+=1
            ascii1+=1
    print()