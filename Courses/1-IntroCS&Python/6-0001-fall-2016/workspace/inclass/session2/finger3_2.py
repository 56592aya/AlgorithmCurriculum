#it is weird with the for loop and so far talked about methods, I could not check for the last character, of course with enumerate it is easy
s = '1.23,2.4,3.123'
total = 0.0
substr = ''
count = 0

while (count != len(s)):
    c = s[count]
    if (c != ','):
        substr = substr+c
        count = count + 1
        #print("substr in first if {}".format(substr))
        if (count == len(s)):
            total = total+float(substr)
    elif(c == ','):
        count = count + 1
        total = total + float(substr)
        substr = ''
    
    
print(total)
