text = input("Enter sentence: ")
words = text.split()
longest_word = []
max_length = 0
for word in words:
    if(len(word)>max_length):
        longest_word = [word]
        max_length = len(word)
    elif(len(word)==max_length):
        longest_word.append(word)
print("Longest word(s): ", longest_word)