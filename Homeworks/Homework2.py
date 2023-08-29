#  я описал в процедурном стиле так как уже знаком с функциями , добавил обработку ошибок


def calculate(a: float, b: float, c: str):
    print(f"Введенные значения {a, b} и операция {c}")
    operations = ["+", "-", "*", "/"]
    if c not in operations:
        c = input("Введите новое значение операции: ")
        while True:
            try:
                a = float(input("Введите новое значение переменной a: "))
                b = float(input("Введите новое значение переменной b: "))
                break
            except ValueError:
                print("Значение должно быть числом.")
        return calculate(a, b, c)
    elif c == operations[0]:
        return a + b
    elif c == operations[1]:
        return a - b
    elif c == operations[2]:
        return a * b
    elif c == operations[3]:
        if b != 0:
            return a / b
        else:
            print("Деление на ноль невозможно.")



while True:
    try:
        a = float(input("Введите новое значение переменной a: "))
        b = float(input("Введите новое значение переменной b: "))
        break
    except ValueError:
        print("Значение должно быть числом. Попробуйте снова.")

operation = input("Введите операцию (+, -, *, /): ")
print("Результат:", calculate(a, b, operation))




def Transform_value(a: float,b: float,c : str):
    regyms=["C","F"]
    if c not in regyms:
        c = input("Введите новое значение операции: ")
        while True:
            try:
                a = float(input("Введите новое значение градусов a: "))
                b = float(input("Введите новое значение градусов b: "))
                break
            except ValueError:
                print("Значение должно быть числом.")
        return Transform_value(a, b, c)
    if c == regyms[0]:
        return a + b
    elif c == regyms[1]:
        return (a - 32) * 5/9 + b


while True:
    try:
        a = float(input("Введите новое значение переменной a: "))
        b = float(input("Введите новое значение переменной b: "))
        break
    except ValueError:
        print("Значение должно быть числом. Попробуйте снова.")

operation = input("Введите операцию (C,F): ")
print("Результат:", calculate(a, b, operation))




def calculate_mix_temperature(v1, t1, v2, t2):
    volume_mix = v1 + v2
    temperature_mix = (v1 * t1 + v2 * t2) / volume_mix
    return volume_mix, temperature_mix


while True:
    try:
        v1 = float(input("Введіть об'єм V1 літрів: "))
        t1 = float(input("Введіть температуру T1: "))
        v2 = float(input("Введіть об'єм V2 літрів: "))
        t2 = float(input("Введіть температуру T2: "))
        break
    except ValueError:
        print("Значение должно быть числом. Попробуйте снова.")
volume_mix, temperature_mix = calculate_mix_temperature(v1, t1, v2, t2)

# Виведення результатів
print(f"Об'єм суміші: {volume_mix} літрів")
print(f"Температура суміші: {temperature_mix}")

