numbers = [5, 8, 12, 20, 25]
target = 12
found = False
for num in numbers:
    if num == target:
        found = True
        break
if found:
    print("Сан табылды")
else:
    print("Сан табылмады")