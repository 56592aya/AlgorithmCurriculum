x = input("enter a binary number: ")
n = len(x)
s = 0
for c in x:
    s += 2**(n-1)*int(c)
    n -= 1
print(s)


