numbers = [3, 5, 8, 12, 15, 20, 25]
target = 15
left = 0
right = len(numbers) - 1
while left <= right:
    middle = (left + right) // 2
    if numbers[middle] == target:
        print("Сан табылды")
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1