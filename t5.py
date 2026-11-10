# завдання 5. порівняння швидкості

import time
import random


def main():
    sizes = [1000, 5000, 10000]

    print("розмір n | пошук list(с) | пошук set(с)  | пошук dict(с) | унікальні list(с)| унікальні set(с)")
    print("-" * 95)

    for n in sizes:
        #підготовка даних
        data_list = list(range(n))
        data_set = set(data_list)
        data_dict = {i: "val" for i in range(n)}

        #шукаємо елемент, якого немає (найгірший випадок)
        target = -1

        #1. пошук у списку
        start = time.perf_counter()
        _ = target in data_list
        time_list = time.perf_counter() - start

        #2. пошук у множині
        start = time.perf_counter()
        _ = target in data_set
        time_set = time.perf_counter() - start

        #3. пошук у словнику
        start = time.perf_counter()
        _ = target in data_dict
        time_dict = time.perf_counter() - start

        #дані з повторами для 2-ї частини
        dup_data = [random.randint(1, n // 2) for _ in range(n)]

        #4. побудова унікальних через список
        start = time.perf_counter()
        u_list = []
        for x in dup_data:
            if x not in u_list:
                u_list.append(x)
        time_u_list = time.perf_counter() - start

        #5. побудова унікальних через множину
        start = time.perf_counter()
        u_set = set()
        for x in dup_data:
            u_set.add(x)
        time_u_set = time.perf_counter() - start

        # вивід таблиці (форматування до 6 знаків після коми)
        print(
            f"{n:<8} | {time_list:<13.6f} | {time_set:<13.6f} | {time_dict:<13.6f} | {time_u_list:<16.6f} | {time_u_set:<15.6f}")


if __name__ == "__main__":
    main()