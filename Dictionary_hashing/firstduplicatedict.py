text = "aaabbbcccdeee"
freq = {}
for char in text:
    if char not in freq:
        freq[char] = 1
    else:
        freq[char] = freq[char]+1
print(freq)
for i in freq:
    if freq[i] == 1:
        print("first non repeated character is ",i)
        break