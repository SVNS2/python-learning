def vowelcount(word):
    vowels = 'aeiouAEIOU'
    count = 0 
    for char in word:
        if char in vowels:
            count+=1
    return count
string = input("Enter a word: ")
print("The number of vowels in the word is:", vowelcount(string))
