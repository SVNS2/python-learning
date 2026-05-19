text = 'aaabbbsbbbaaa'
freq={}
first_char = ''
for ch in text:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] = freq[ch]+1
rep = []
for key in freq:
    if(freq[key] == 1):
        first_char = key
        break

print(first_char)