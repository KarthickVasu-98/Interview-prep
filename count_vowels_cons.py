s = str(input("Enter the string: "))
vowels = 0
cons = 0

for i in s:
  if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A'or i=='E' or i=='I' or i=="O" or i=="U":
    vowels = vowels+1
  else:
    cons = cons+1

print("Total Vowels: ",vowels)
print("Total Cons: ",cons)
