print("enter x:")
x = int(input())
print("enter y:")
y = int(input())
print("enter z:")
z = int(input())
res = float("-inf")
if (x % 2 == 1):
    res = x
elif(y % 2 == 1 and y > res):
    res = y
elif (z % 2 == 1 and z > res):
    res = z
if res == float("-inf"):
    print("none of them is the answer")
else:
    print("the answer is {}".format(res))

