#input() returns a string so if we want it as an int or floar we should specifically say that
#print("enter a number:")
#s = input()
#print(type(s))
#s = int(input())
#print(type(s))

#multiline comment
'''
#similar ways of doing the same thing
num = int(input())
print("using just the integer")
print("the number is", num)
print("using conversion to string")
print("the number is", str(num))
print("using %s with integer")
print("the number is %s"% num)
print("using the %s with string")
print("the number is %s"%str(num))
print("using %d for num")
print("the number is %d"%num)
print("using str.format(num) with {0} placeholder")
print("the number is {0}".format(num))
print("using str.format(num) with {} placeholder")
print("the number is {}".format(num))
'''
import math
print("Enter number x:")
x = int(input())
print("Enter number y:")
y=int(input())
xpowy = x**y
log2x = int(math.log2(x))
print("{}".format(xpowy))
print("{}".format(log2x))
