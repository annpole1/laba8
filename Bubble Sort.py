def bubble_sort(mas):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(mas) - 1):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
                swapped = True


arr = [1, 6, 1, -6, 14, -4, 3, 11, 2, -7]
bubble_sort(arr)
for number in arr:
    print(number, end=' ')
