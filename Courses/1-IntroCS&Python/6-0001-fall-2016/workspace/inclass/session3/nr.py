## imagine the polynomial given is x**2 - 24 = 0
guess = 0.1
iter =0
while abs(guess**2 - 24)>0.0001 :
    guess -= (guess**2- 24)/(2*guess)
    iter +=1
print("guess is {} and approx to 24 is {}".format(guess, guess**2))
print(iter)
