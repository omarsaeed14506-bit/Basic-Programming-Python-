sentence = input("Please enter a sentence: ")
sentence = sentence.lower()
words = sentence.split()
expected = {}
for word in words:
    if word in expected:
        expected[word] += 1
    else:
        expected[word] = 1
print("Expected:",expected)