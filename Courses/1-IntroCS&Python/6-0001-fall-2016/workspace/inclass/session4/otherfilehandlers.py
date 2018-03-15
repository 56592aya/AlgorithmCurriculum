nameHandle = open("kids", "r")
x = nameHandle.readlines()
print("readlines ",type(x))
nameHandle.close()

nameHandle = open("kids", "r")
x = nameHandle.readline()
print("readline ", type(x))
nameHandle.close()

nameHandle = open("kids", "r")
x = nameHandle.read()
print("read ", type(x))
nameHandle.close()


nameHandle = open("kids", "r")
nameHandle2 = open("kids2", "w")

x = nameHandle.readlines()
nameHandle2.writelines(x)
nameHandle.close()
nameHandle2.close()

