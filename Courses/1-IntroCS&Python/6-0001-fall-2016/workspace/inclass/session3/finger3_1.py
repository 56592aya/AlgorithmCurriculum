x = int(input("enter an integer: "))
pwr = 1
root = 2
found = False
while root < x and not found:
    #print("starting first while the root is {} and pwr is {}".format(root, pwr))
    while  root**pwr <= x and pwr < 6:
        #print("second while root is {} and pwr is {}".format(root, pwr))
        if (root**pwr == x):
            print("found root {} and pwr {}".format(root, pwr))
            found=True
            break
        else:
            pwr = pwr+1
    root = root+1
    if (root == x):
        found = False
        print("not found")
        break
    pwr = 1




