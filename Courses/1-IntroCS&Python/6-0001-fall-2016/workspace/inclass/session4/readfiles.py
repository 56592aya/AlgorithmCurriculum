nameHandle = open("kids", "r")
for line in nameHandle:
    print(line)
nameHandle.close()
#avoid extra new line
nameHandle = open("kids", "r")
for line in nameHandle:
    print(line[:-1])
nameHandle.close()

