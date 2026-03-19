def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


values = [5, 2, 9, 1, 3]
sorted_values = bubble_sort(values)

print("Sorted list:", sorted_values)
