def palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False
s = input("Enter a word: ")
if palindrome(s):
    print(f"{s} is a palindrome.")
else:    
    print(f"{s} is not a palindrome.")