sentence = input("enter a sentence: ")
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
digits_count = 0
space_count = 0
for char in sentence.lower():
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    elif char.isdigit():
        digits_count += 1
    elif char.isspace():
        space_count += 1
print("Vowels:",vowel_count)
print("Consonants:",consonant_count)
print("Digits:",digits_count)
print("Spaces:",space_count)