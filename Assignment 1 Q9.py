list1 = [1, 2, 3, 4, 5, 8]
list2 = [3, 4, 5, 6, 7, 8]
common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)
common_tuple = tuple(common_elements)
print("Expected tuple:", common_tuple)
