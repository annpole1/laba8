import math


def shell_sort(mas):
    n = len(mas)
    k = int(math.log2(n))
    step = 2 ** k - 1
    while step > 0:
        for i in range(step, n):
            temp = mas[i]
            j = i
            while j >= step and mas[j - step] > temp:
                mas[j] = mas[j - step]
                j -= step
            mas[j] = temp
        k -= 1
        step = 2 ** k - 1


arr = [1, 6, 1, -6, 14, -4, 3, 11, 2, -7]
shell_sort(arr)
for number in arr:
    print(number, end=' ')
