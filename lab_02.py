import math

def task_1():
    while True:
        try:
            a = int(input("Перше ціле число: "))
            b = int(input("Друге ціле число: "))
            c = int(input("Третє ціле число: "))
            result = [x for x in (a, b, c) if 1 <= x <= 3]
            print("Числа які належать інтервалу", result)
            break
        except ValueError:
            print("Помилка")

def task_2():
    while True:
        try:
            year = int(input("Введіть рік: "))
            if year < 0:
                print("Помилка")
                continue
            print("Високосний" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "Не високосний")
            break
        except ValueError:
            print("Помилка")

def task_3():
    while True:
        try:
            price = int(input("Введіть ціну: "))
            if price < 0:
                print("Помилка: ціна не може бути від'ємною.")
                continue
            if price < 500:
                print(price)
            elif price > 1000:
                print(price * 0.95)
            else:
                print(price * 0.97)
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_4():
    while True:
        try:
            numbers = [int(input(f"Введіть число {i+1}: ")) for i in range(4)]
            min_num = min(numbers)
            print("Найменше число:", min_num)
            print("Косинус", min_num, "радіан", math.cos(min_num))
            break
        except ValueError:
            print("Помилка")

def task_5():
    while True:
        try:
            numbers = [int(input(f"Введіть число {i+1}: ")) for i in range(3)]
            max_num = max(numbers)
            print("Найбільше число:", max_num)
            print("Синус", max_num, "радіан", math.sin(max_num))
            break
        except ValueError:
            print("Помилка")

def task_6():
    while True:
        try:
            a = int(input("Довжина ребер: "))
            b = int(input("Довжина основи: "))
            if a < 0 or b < 0 or b >= 2 * a:
                print("Помилка")
                continue
            area = (b * math.sqrt(4 * a**2 - b**2)) / 4
            if area % 2 == 0:
                print(f"Площа трикутника поділена на 2 = {area / 2}")
            else:
                print("Не можу ділити на 2!")
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_7():
    while True:
        try:
            number = int(input("Введіть число (1-12): "))
            if number < 1 or number > 12:
                print("Число не відповідає проміжку")
                continue
            months = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
            print(months[number - 1])
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_8():
    while True:
        try:
            numbers = [int(input(f"Введіть число {i+1}: ")) for i in range(3)]
            positives = sum(1 for x in numbers if x > 0)
            print("Кількість позитивних чисел:", positives)
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_9():
    while True:
        try:
            a = int(input("Введіть число а (a<b): "))
            b = int(input("Введіть число b (a<b): "))
            if a > b:
                print("Помилка")
                continue
            print(f"Сума всіх чисел між {a} та {b}: {sum(range(a, b + 1))}")
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_10():
    while True:
        try:
            a = int(input("Введіть число а (a<b): "))
            b = int(input("Введіть число b (a<b): "))
            if a > b:
                print("Помилка")
                continue
            sum_squares = sum(i**2 for i in range(a, b + 1))
            print(f"Сума квадратів чисел від {a} до {b}: {sum_squares}")
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_11():
    while True:
        try:
            a = int(input("Введіть число а (a<=200): "))
            b = int(input("Введіть число b: "))
            if a > b or a > 200:
                print("Помилка")
                continue
            count = b - a + 1
            sum_numbers = sum(range(a, b + 1))
            average = sum_numbers / count
            print(f"Середнє арифметичне чисел від {a} до {b}: {average}")
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_12():
    while True:
        try:
            a = int(input("Введіть число a (b ≥ a): "))
            b = int(input("Введіть число b (b ≥ a): "))
            if b < a:
                print("Помилка")
                continue
            sum_result = 0
            initial_a = a
            while a <= b:
                sum_result += a
                a += 1
            print(f"Сума всіх чисел від {initial_a} до {b}: {sum_result}")
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_13():
    while True:
        try:
            a = int(input("Введіть число а (0 ≤ a ≤ 50): "))
            if a < 0 or a > 50:
                print("Помилка")
                continue
            sum_squares = sum(i**2 for i in range(a, 51))
            print(f"Сума квадратів чисел від {a} до 50: {sum_squares}")
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_14():
    while True:
        try:
            N = int(input("Введіть ціле число N (> 1): "))
            if N <= 1:
                print("Помилка")
                continue
            K = 0
            while 5 ** K <= N:
                K += 1
            print(f"Найменше K, для якого 5^{K} > {N}: {K}")
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")

def task_15():
        while True:
            try:
                n = int(input("Введіть число n: "))
                for i in range(1, 100):
                    square = i ** 2
                    if square > n:
                        print(f"Перше число більше {n}: {square}")
                        break
                break
            except ValueError:
                print("Помилка: введіть лише числові значення.")

def task_16():
    while True:
        try:
            n = int(input("Введіть число n: "))
            i, current = 1, 1
            while current <= n:
                i += 1
                current += i * 2 - 1
            print(f"Перше число більше {n}: {current}")
            break
        except ValueError:
            print("Помилка: введіть лише числові значення.")
tasks = [
    task_1, task_2, task_3, task_4, task_5,
    task_6, task_7, task_8, task_9,
    task_10, task_11, task_12, task_13, task_14, task_15, task_16
]


for i, task in enumerate(tasks, 1):
    print(f"\nВиконання завдання {i}:")
    task()
