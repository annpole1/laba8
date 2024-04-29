def insertion_sort(mas):
    for i in range(1, len(mas)):
        item_to_insert = mas[i]
        j = i - 1
        while j >= 0 and mas[j] > item_to_insert:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = item_to_insert


arr = [1, 6, 1, -6, 14, -4, 3, 11, 2, -7]
insertion_sort(arr)

for number in arr:
    print(number, end=' ')
