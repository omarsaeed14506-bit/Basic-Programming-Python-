grade = [75, 48, 90, 62, 35, 88, 51]
passed = 0
failed = 0
for g in grade:
    print(g)
    if g >= 50:
        passed += 1
    else:
        failed += 1
print("Passed:", passed)
print("Failed:", failed)