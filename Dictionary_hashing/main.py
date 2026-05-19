Age = int(input("Enter your age: "))
Name = input("Enter your name: ")
Percentage = float(input("Enter your percentage: "))
print('Hello', Name)
if (Age >= 18):
    if(Percentage >= 60):
        print("You are eligible for the scholarship.")
    else:
        print("You are not eligible for the scholarship.")
else:
    print('you are underage')