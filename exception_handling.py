#error types = compile time, logical and runtime
#exceptional handling is used to bypass runtime error
#exception = unwanted or unexpected event occurs during the execution of the program
#objective of exceptional handling = even if we getting an error, the execution should not stop
#compile time error is easiest to find, then logical abd then runtime
#two types of statement in exceptional handling, normal statement = in which error would not occur, critical statement = in which error may occur
#critical statements can be handled by try catch block
a = 5
b = 2

try:        #to catch error
    print('resource open')
    print(a/b)
    k = int(input('enter a number : '))

except ZeroDivisionError as e: #to do after an error has occured,e here is an representation of object Exception, ZeroDivisonError comes under Exception types
    print('error is :', e)
except ValueError as e:
    print('error is :', e)
except Exception as e:
    print('something went wrong.....')

finally:        #execute statements does not matter if error has occured or not
    print('resource close')

print('bye')