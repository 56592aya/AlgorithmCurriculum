#Difference between declarative knowledge and imperative knowledge
#Declarative:square root of a number x is y such that y*y = x
#imperative requires the recipe
#i.e
#1)start with a guess g
#if g*g is close enough to x stop and say g is the answer
#otherwise make a new guess by averaging g and x/g
#using the new guess repeat the process untile close enough

#my writing first
import random
x = 16.0
g = random.uniform(1, x)
print("first g is" ,g)
print("and the square is ", g*g)
while (True):
    if (abs(g*g - x) < 1e-12):
        #close enough
        print("final g is ", g)
        break
    else:
        g = .5*(g+x/g)
        print("new g is ", g)


