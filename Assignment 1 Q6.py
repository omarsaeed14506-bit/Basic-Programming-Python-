numbers = [5, 2, 5, 8, 2, 10, 8, 12]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Expected:",unique_numbers)