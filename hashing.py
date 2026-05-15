text = 'programming'
freq={}
for i in text:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] = freq[i]+1
print(freq)
