x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))

if x>y :
    if x>z :
        print("1st is greatest")
    else:
        print("3rd is greatest")
else:
    if y>z :
        print("2nd is greatest")
    else:
        print("3rd is greatest")