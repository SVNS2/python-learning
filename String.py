a = input("Enter a string: ")
temp = a
c = ""
for i in range(len(a)-1, -1, -1):
    c = c + a[i]
if (c == temp):
    print("The string is a palindrome.")
else:    print("The string is not a palindrome.")    
    
