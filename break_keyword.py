av=10

x=int(input("How many candies do you want?  "))

i=1
while i<=x:
    if i>av:
        print("\nSorry we are out of stock")
        break
    print('Candy', end="  ")
    i+=1

print("bye")