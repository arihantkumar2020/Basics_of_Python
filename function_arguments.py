
def update(x):
    print("id of x =", id(x))
    x = 9
    print("id of x after modification =", id(x))
    print("x =",x)

def update2(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))
    print(lst)

str = input("Enter type : ")
if str == "integer" :
    a = 10
    print("id of a =", id(a))
    update(a)
    print("a =", a)

elif str == "list":
    lst = [10, 20, 30]
    print(id(lst))
    update2(lst)
    print(lst)