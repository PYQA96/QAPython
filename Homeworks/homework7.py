import math


def sum_range(start: float, end: float):
    if start > end:
        start, end = end, start
    return sum([float(i) for i in range(int(start), int(end) + 1)])


def square(side):
    if side<=0:
        raise ValueError("Сторона не может быть 0")
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal


def display_box(width: int, height: int, character="*"):
    if width < 2 or height < 2:
        print("Неприпустимі розміри для прямокутника.")
        return f"Ошибка вычисления"

    print(character * width)
    for i in range(1, height - 1):
        print(character + " " * (width - 2) + character)
    if height > 1:
        print(character * width)


def my_map(function,iterable):
    try:
        if not callable(function):
            raise ValueError("Функцию невозможно вызвать")
        return [function(item) for item in iterable]
    except Exception as e:
            raise ValueError("Ошибка при применении функции к итерируемому объекту:", e)



if __name__ == '__main__':

    try:
        start = float(input("Введите переменную 1:"))
        end = float(input("Введите переменную 2:"))
        result = sum_range(start, end)
        print(result)
    except ValueError as e:
        print(f"Ошибка:переменная должна быть числом {e}")

    try:
        side = float(input("Введите сторону:"))
        result = square(side)
        print(*result)
    except ValueError as e:
        print(f"Ошибка: Сторона должна быть числом")

    try:
        width = int(input("Введите ширину прямокутника:"))
        height = int(input("Введите висоту прямокутника:"))
        character = input("Введите символ для ліній (за замовчуванням '*'): ")
        if not character:
            character = "*"
        display_box(width, height, character)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        function_str = input("Введите Функцию (например, 'lambda x: x ** 2'): ")
        iterable_str = input("Введите итерируемую последовательность (например, [1, 2, 3, 4, 5]): ")

        function = eval(function_str)
        iterable = eval(iterable_str)

        if not callable(function):
            raise ValueError("Функцию невозможно вызвать")
        if not isinstance(iterable, list):
            raise ValueError("Это не список")

        result = my_map(function, iterable)
        print(result)
    except (Exception,ValueError) as e:
        print("Произошла ошибка:", e)