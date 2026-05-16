text = "hello"
result = " "
count = 0
for char in text:
    if char not in result:
        result += char
    elif char in result:
        count = count+1
print(result)
print("number of duplicates removed:",count)