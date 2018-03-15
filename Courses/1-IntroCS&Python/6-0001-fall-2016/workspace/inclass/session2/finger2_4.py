num=10
res = float("-inf")
while (num != 0):
    curr = int(input())
    if (curr % 2 == 1 and curr > res):
        res = curr
    num = num-1
if (res == float("-inf")):
    print("nothing found")
else:
    print("result is {}".format(res))
