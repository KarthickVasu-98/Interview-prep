s = str(input('Enter the String: '))
r = ''

for i in range(len(s)):
    if s[i] in r:
        print(s[i],'is duplicate')
        i+=1
    else:
        r = r+s[i]
print('there is no duplicate in this string')
