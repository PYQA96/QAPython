class IsNotOperation(Exception):
    pass


def calculate(first: float, second: float, operand: str):
    print(f"Введенные значения {first}, {second} и операция {operand}")
    operations = ["+", "-", "*", "/"]
    result = None
    if operand == operations[0]:
        result = first + second
    elif operand == operations[1]:
        result = first - second
    elif operand == operations[2]:
        result = first * second
    elif operand == operations[3]:
        if second != 0:
            result = first / second
        else:
            print("Деление на ноль невозможно.")
    return f"Результат {result if result is not None else 'Ошибка'}"


variable_names = ["первой", "второй"]
variables_value = []
number_of_operation = 0
while len(variables_value) < 2:
    try:
        value = float(input(f"Введите значение {variable_names[number_of_operation]} переменной: "))
        variables_value.append(value)
        number_of_operation += 1
    except ValueError:
        print("Значение должно быть числом.")

operations = ["+", "-", "*", "/"]
variables_operation = []
while True:
    try:
        value = input(f"Введите значение операции {operations}: ")
        if value in operations:
            variables_operation.append(value)
            break
        else:
            raise IsNotOperation
    except IsNotOperation:
        print(f"Неверная операция. Попробуйте снова, операции должны быть только {operations} ")

first_variable, second_variable = variables_value[0], variables_value[1]
operation = variables_operation[0]
result = calculate(first_variable, second_variable, operation)
print(result)


def transform_value(first: float, operand: str):
    print(f"Введенные значения {first} и операция {operand}")
    regyms = ["c", "f"]
    result = None
    if operand == regyms[0]:
        result = first + 273.15
    elif operand == regyms[1]:
        result = (first * 9 / 5) + 32
    return f"Результат {result}"


variables_value = None
while True:
    try:
        value = float(input(f"Введите значение первой переменной: "))
        variables_value = value
        break
    except ValueError:
        print("Значение должно быть числом.")

operations = ["c", "f"]
variables_operation = None
while True:
    try:
        value = input(f"Введите значение операции {operations}: ").lower()
        if value.lower() in operations:
            variables_operation = value
            break
        else:
            raise IsNotOperation
    except IsNotOperation:
        print(f"Неверная операция. Попробуйте снова, операции должны быть только {operations} ")

result = transform_value(variables_value, variables_operation)
print(result)


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

# Вывод результатов
print(f"Об'єм суміші: {volume_mix} літрів")
print(f"Температура суміші: {temperature_mix}")
