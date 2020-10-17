def rev(s):
    if s=="":
        return s
    else:
        a=""
        l = s[len(s)-1]
        a = a+l
        print(a, end= "")
        return rev(s[0:len(s)-1])
s = str(input("Enter the String: "))
print(rev(s))
