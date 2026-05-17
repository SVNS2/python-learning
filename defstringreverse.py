def reversestring(s):
    for char in range(len(s)-1,-1,-1):
        print(s[char], end="")
b = input("Enter a string: ")
reversestring(b)

