import timeit
import memory_profiler
from cpuinfo import get_cpu_info
from random import randint


@memory_profiler.profile
def sort(mas):
    count = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(mas) - 1):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
                swapped = True
                count += 1
    return arr, count


l3_cache_size = get_cpu_info()['l3_cache_size'] // 1024 // 1024

min_size = l3_cache_size * 2
step = l3_cache_size * 2
max_size = l3_cache_size * 20

for i in range(min_size, max_size + 1, step):
    arr = [randint(1, 50) for x in range(i)]
    time_start = timeit.default_timer()
    arr, count = sort(arr)
    time_end = timeit.default_timer()
    print(f'Время выполения: {time_end - time_start}')
    print(f'Кол-во операций: {count}')
    print(arr)
