text1 = input("enter the first word: ")
text2 = input("enter the second word: ")
freq1 = {}
freq2 = {}
text1 = text1.lower()
text2 = text2.lower()
if len(text1)!=len(text2):
     print("they are not anagrams")
else:
    for char in text1:
        if char not in freq1:
            freq1[char]=1
        else:
            freq1[char]+=1
    for char in text2:
        if char not in freq2:
            freq2[char]=1
        else:
            freq2[char]+=1
    if freq1==freq2:
     print("they are anagrams")
    else:
        print("they are not anagrams")