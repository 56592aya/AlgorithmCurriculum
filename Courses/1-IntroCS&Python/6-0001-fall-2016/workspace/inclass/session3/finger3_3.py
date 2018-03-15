#cube root using something like bisection
x= int(input("enter and integer:"))
epsilon = 0.01
numGuesses = 0
if x < 0:
    low = min(-1, x)
    high = 0.0
else:
    low = 0.0
    high = max(1.0, x)

ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print("low ",low," ,high ",high," ans ",ans)
    numGuesses += 1
    if x < 0:
        if ans**3 < x:
            low = ans
        else:
            high = ans
    else:
        if ans**3 < x:
            low = ans
        else:
            high = ans
    ans = (high+low)/2.0


print("numGuesses is {}".format(numGuesses))

print("{} is close to square root of {}".format(ans,x))
