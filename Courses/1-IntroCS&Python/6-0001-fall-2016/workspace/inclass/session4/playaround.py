#to check out the return value and type of a function
def weird_func(x):
    if x > 0:
        return("positive")

x = 2
res = weird_func(x)
print("result {}, and type {}".format(res,type(res)))
x = -2
res = weird_func(x)

print("result {}, and type {}".format(res,type(res)))
##
###use of keyword argument and defaults
def printnames(firstname,lastname, reverse=False):
    if reverse:
        print(lastname, " ", firstname)
    else:
        print(firstname, " ", lastname)

printnames("arash", "yazdiha")
printnames("arash", "yazdiha", reverse=True)
printnames("arash", "yazdiha", True)
#printnames(reverse=True,"arash", "yazdiha")
#printnames(reverse=False,"arash", "yazdiha")


##### static or lexical scoping, this a very good example
def f(x):
    def g():
        x="abc"
        print("x is {}".format(x))
    def h():
        z = x
        print("z is {}".format(z))
    x = x+1
    print("x is {}".format(x))
    h()
    g()
    print("x is {}".format(x))
    return g

x = 3
z = f(x)
print("x is {}".format(x))
print("z is {}".format(z)) 
z()

