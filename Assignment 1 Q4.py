numbers = [15, 42, 8, 91, 23, 4, 55]
largest = numbers[0]
smallest = numbers[0] 
for num in numbers:
    if num > largest:
        largest = num 
    if num < smallest:
        smallest = num
print("largest number is:",largest)
print("smallest number is:",smallest)