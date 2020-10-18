s = str(input("Enter the string: "))
val = str(input("Enter the char which you want to count: "))
count = 0

for i in s:
    if i==val:
        count = count+1

print(val, "is repeated", count,"times")
