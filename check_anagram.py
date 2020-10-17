s1 = str(input('Enter the string1: '))
s2 = str(input('Enter the string2: '))
a = sorted(s1)
b = sorted(s2)


if a==b:
    print('Anagram')
else:
    print('Not a anagram')
