#while loop
i = 0
numbers = []
while i < 6:
    print(f"i at top is {i}")
    numbers.append(i)
    i = i+1
    print("numbers now :", numbers)
    print(f"at the bottom is {i}")

print("The numbers:")
for num in numbers:
    print(num)
