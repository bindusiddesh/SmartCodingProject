# Multiply 3 and any number
def mult(number):
    mult = number * 3
    print("Product of number with 3 is %s" % mult)
    return mult

    
# adds two numbers together
def add(a, b):
    sum = a + b
    print("Sum of numbers is %s" % sum)
    return sum


# Data structure
numbers = [1,2,3,6]
def sumOfListNumbers(someList):
    length = len(someList)
    sum = 0
    for i in range(length):
        sum += someList[i]
    print("Sum of numbers in list is %s" % sum)
    return sum

    

# Program checker (do not change the lines below)    
assert sumOfListNumbers(numbers) == 12
assert mult(3) == 9
assert add(1,3) == 4
