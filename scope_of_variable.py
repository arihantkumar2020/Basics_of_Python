a = 10      #global variable
b = 20      #global variable
c = 15      #global variable

def something():
    b=30        #local variable
    print("printing b", b)      #preference will always be given to local variable
    global a        #use of global variable
    a=20
    print("printing global", a)

#using global concept it is not possible to use local and global variable inside the same function
#so we will use globals() function here
def newfunction():
    x = globals()       #now x will have all global variables' data
    #using global variable here
    globals()['c'] = 1000
    print("modified global variable", c)



something()
print("outside b", b)
print("outside a", a)

#using global and local variable in the same function
newfunction()