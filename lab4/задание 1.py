from math import factorial

# 1. Создайте список квадратов первых 10 натуральных чисел (list comprehension)
squares = [x**2 for x in range(1, 11)]
print(f"1. {squares}") # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2. Создайте словарь, содержащий названия дней недели и их порядковые номера (dict comprehension)
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day = {day: i+1 for i, day in enumerate(days)}
print(f"2. {day}")

# 3. Создайте множество, содержащее теги библиотек в нижнем регистре (list comprehension)
libraries = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags = {library.lower() for library in libraries}
print(f"3. {tags}")

# 4. Создайте список, содержащий только четные числа из исходного списка (list comprehension)
numbers = [1, 3, 4, 87, 98, 15, 7, 4]
evens_numbers = [x for x in numbers if x % 2 == 0]
print(f"4. {evens_numbers}")

# 5. Создайте словарь, где ключи — это числа от 1 до 5, а значения — их факториалы (list comprehension)
factorials = {n: factorial(n) for n in range(1, 6)}
print(f"5. {factorials}")