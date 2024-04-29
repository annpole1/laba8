def partition(mas, low, high):
    pivot = mas[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while mas[i] < pivot:
            i += 1

        j -= 1
        while mas[j] > pivot:
            j -= 1

        if i >= j:
            return j

        mas[i], mas[j] = mas[j], mas[i]


def quick_sort(mas, low, high):
    if low < high:
        split_index = partition(mas, low, high)
        quick_sort(mas, low, split_index)
        quick_sort(mas, split_index + 1, high)


arr = [1, 6, 1, -6, 14, -4, 3, 11, 2, -7]
quick_sort(arr, 0, len(arr) - 1)

for number in arr:
    print(number, end=' ')
