t1 = ()
t2 = (1, "two", 3)
print(t1)
print(t2)
t3 = (t1, 2)
print(t3)
#specifically this one is important
t4 = (1)
#prints only 1 and not (1), since (1) is just a singleton element 1
print(t4)
print(type(t4))
#to denote a single element inthe tuple, you shoudl add a comma at the end
t5 = (1,)
print(t5)
print(type(t5))

t1 = (1, "two", 3)
t2 = (t1, 3.25)
print(t2)
#like (1) the following two are the same
#also + like in strings concatenates
print(t1+t2)
print((t1+t2))
print((t1+t2)[3])

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1+t2)
def findDivisors(n1, n2):
    """Assuems that n1, and n2 are positive ints, return a tuple containing all common divisors of n1 and n2"""
    divisors=()
    for i in range(1, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            divisors = divisors+(i,)
    return divisors
divisors = findDivisors(20, 100)
print(divisors)
total = 0
for d in divisors:
    total +=d
print(total)

#multiple assignment example

def findExtremeDivisors(n1, n2):
    divisors = ()
    minVal, maxVal = (None, None)
    for i in range(2, min(n1, n2)+1):
        if n1%i == 0 and n2 % i == 0:
            if minVal == None or i < minVal :
                minVal = i
            if maxVal == None or i > maxVal :
                maxVal = i
    return (minVal, maxVal)

minDivisor, maxDivisor = findExtremeDivisors(100, 200)
print(minDivisor)
print(maxDivisor)


x = [1,2,3]
y = [5,6,7]
#the elements of the z are not copies of x, y, it is them
z = [x,y]
w = [[1,2,3],[5,6,7]]
print (z == w)
print (id(z) == id(w))

#To see why the elements of z are not copies and are the lists x, and y themselves, see this below:
x.append(4)
print(z)
#the above is known as aliasing, we have access to the same list object through two different paths

#append, concatnation and extend
x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

print("x is {}".format(x))
print("y is {}".format(y))
print("append, x, y {}".format(x.append(y)))
#it does it but for printing it prints None, i wonder why
print("x is {}".format(x))
x = [1,2,3]
print("x is {}".format(x))
print("y is {}".format(y))
print("x+y is {}".format(x+y))
print("x is {}".format(x))
print("y is {}".format(y))
print("extended x by y is {}".format(x.extend(y)))
print("x is {}".format(x))
print("y is {}".format(y))

def wrongDupRemove(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
L1=[1,2,3,4]
L2=[1,2,5,6]
wrongDupRemove(L1, L2)
print(L1)
def rightDupRemove(L1, L2):
    for e in L1[:]:
        if e in L2:
            L1.remove(e)

L1=[1,2,3,4]
L2=[1,2,5,6]
rightDupRemove(L1, L2)
print(L1)

#list comprehension
mixed= [1, 2, "a", 3, 4.0]
print ([x**2 for x in mixed if type(x) == int])


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
L = [1, -2, 3.33]
print(L)
applyToEach(L, abs)
print(L)

L = [1, -2, 3.33]
print(L)
applyToEach(L, str)
print(L)

L = [1, -2, 3.33]
print(L)
applyToEach(L, int)
print(L)

L = [1, -2, 3.33]
print(L)
applyToEach(L, lambda x : x**2)
print(L)

res = list(map(lambda x: x**2 ,[1,2,3]))
print(res)

res = list(map(min, [1,20, 40], [2, 21, 39]))

print(res)

s = "Hello my Name is aRASH"
print(s)
print(s[3:5])
print(len(s))
print(s.count("e"))
print(s.find("e"))
print(s.find("j"))
print(s.rfind("e"))
print(s.index("e"))
#print(s.index("j")) error
print(s.rindex("e"))
print(s.lower())
s = "Hello my Name is aRASH"
print(s.replace("aRASH", "Ashi"))
s = "Hello my Name is  aRASH    "
print(s.rstrip())
print(s)
print(s.split(" "))
print(s)
print(s.split())

monthNumbers = {3:"Mar", 2:"Feb", 4:"Apr", 1:"Jan", 5:"May"} 
print(monthNumbers.keys())
keys = []
for e in monthNumbers:
    keys.append(e)
print(keys)
keys.sort()
print(keys)









