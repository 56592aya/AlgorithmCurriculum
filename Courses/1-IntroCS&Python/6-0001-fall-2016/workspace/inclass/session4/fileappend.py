nameHandle = open('kids', 'a')
nameHandle.write("Ashi\n")
nameHandle.write("Papar\n")
nameHandle.close()
nameHandle = open('kids','r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()


