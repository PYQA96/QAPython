#  я описал в процедурном стиле так как уже знаком с функциями , добавил обработку ошибок
# Создал своё исключние
class Isnotoperation(Exception):
    pass


def calculate(first: float, second: float, operand: str):
    print(f"Введенные значения {first, second} и операция {operand}")
    operations = ["+", "-", "*", "/"]
    result=None
    if operand == operations[0]:
        result= first + second
    elif operand == operations[1]:
        result= first - second
    elif operand == operations[2]:
        result= first * second
    elif operand == operations[3]:
        if second != 0:
            result= first / second
        else:
            print("Деление на ноль невозможно.")
    return f"Результат {result if result is not None else 'Ошибка' }"

# тут можно было сделать и через два цыклв , но я решил использовать 1 и счетчик переменных number_of_opeation
variable_names = ["первой", "второй"]
variabels_value = []
number_of_opeation = 0
while len(variabels_value) < 2:
    try:
        value = float(input(f"Введите значение {variable_names[number_of_opeation]}  переменной: "))
        variabels_value.append(value)
        number_of_opeation = number_of_opeation + 1
    except ValueError:
        print("Значение должно быть числом.")
operations = ["+", "-", "*", "/"]
variabels_operation = []
while True:
    try:
        value = input(f"Введите значение операции {operations}: ")
        if value in operations:
            variabels_operation.append(value)
            break
        else:
            raise Isnotoperation
    except Isnotoperation:
        print(f"Неверная операция. Попробуйте снова, операции должны быть только {operations} ")
first_varibale, second_varible = variabels_value[0], variabels_value[1]
operation = variabels_operation[0]
result = calculate(first_varibale, second_varible, operation)
print(result)

def Transform_value(first: float, operand: str):
    print(f"Введенные значения {first} и операция {operand}")
    regyms = ["c", "f"]
    result=None
    if operand == regyms[0]:
        result=first + 273.15
    elif operand == regyms[1]:
        result=(first * 9/5) + 32
    return f"Результат {result}"


variabels_value = None
while True:
    try:
        value = float(input(f"Введите значение первой  переменной: "))
        variabels_value=value
        break
    except ValueError:
        print("Значение должно быть числом.")
operations = ["c", "f"]
variabels_operation = None
while True:
    try:
        value = input(f"Введите значение операции {operations}: ").lower()
        if value.lower() in operations:
            variabels_operation=value
            break
        else:
            raise Isnotoperation
    except Isnotoperation:
        print(f"Неверная операция. Попробуйте снова, операции должны быть только {operations} ")
result=Transform_value(variabels_value,variabels_operation)
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

# Виведення результатів
print(f"Об'єм суміші: {volume_mix} літрів")
print(f"Температура суміші: {temperature_mix}")
