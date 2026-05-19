def anagram(word1, word2):
    if sorted(word1.lower())==sorted(word2.lower()):
        return True
    else:
        return False
word1 = input("Enter a string:")
word2 = input("Enter another string:")
if anagram(word1, word2):
    print("The two words are anagrams.")
else:
    print("They are not anagrams.")
