def some_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"\nФункция {func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Площадь прямоугольника: {result}")
        return result

    return wrapper

@some_decorator
def calculate_area(length, width):
    return length * width
def parameters():
    try:
        length = float(input("Введите длину: "))
        width = float(input("Введите ширину: "))
        return length, width
    except ValueError:
        print("Ошибка! Введите числа.")
        return parameters()
def main():
    length, width = parameters()
    calculate_area(length, width)
main()