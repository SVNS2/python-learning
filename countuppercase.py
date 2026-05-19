def uppercase_count(word):
    count = 0
    for char in word:
        if char.isupper():
            count+=1
    return count
q = input("Enter a word:")
q = uppercase_count(q)
print(f"The number of uppercase letters in the word is: {q}")