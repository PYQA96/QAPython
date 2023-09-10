str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
result1 = {}
result2 = {}
result3={}
square_list = list(map(lambda x: int(x) ** 2, str_list))

# 1) вариант
for key in str_list:
    square = lambda key: int(key) ** 2
    result1[key] = square(key)
print(result1)
# 2) вариант сложить через комперхеншн
result2 = {i: int(i) ** 2 for i in str_list}
print(result2)

# 3 вариант сложил 2 списка
merge_str = {str_list[i]: square_list[i] for i in range(len(str_list))}
print(merge_str)

# 4 вариант
for list1,list2 in zip(str_list,square_list):
    result3[list1]=list2
print(result3)



# калькулятор
class FormulaError(Exception):
    pass


class WrongOperatorError(Exception):
    pass


class EmptyOperands(Exception):
    pass


def calculate(formula):
    try:
        num1, operator, num2 = formula.split()
        num1 = float(num1)
        num2 = float(num2)

        if operator not in ('*', '/'):
            raise WrongOperatorError("Невірний оператор, будь ласка, використовуйте '*' або '/'.")

        if operator == '/' and num2 == 0:
            raise ZeroDivisionError("Ділення на нуль заборонено.")

        if operator == '*':
            result = num1 * num2
        else:
            result = num1 / num2

        return result

    except ValueError:
        raise FormulaError("Невірний формат введення. Будь ласка, введіть формулу у форматі 'число оператор число'.")
    except FormulaError as e:
        return str(e)


attempts = 3
for _ in range(attempts):
    formula = input("Введіть формулу (наприклад, 2 * 5): ")
    try:
        result = calculate(formula)
        print(f"Результат: {result}")
    except FormulaError as e:
        print(f"Помилка: {e}")

    retry = input("Бажаєте спробувати ще раз? (так/ні): ").lower()
    if retry != 'так':
        break
count_of_input = 0
variables_to_calculate = None
firs_operand, operation, second_operand = None, None, None
while count_of_input < 3:
    try:
        count_of_input = count_of_input + 1
        variables_to_calculate = input("Введите данные в формате (число,выражение,число) через пробел: ").split()
        variables_to_calculate = list(map(lambda x: int(x) if x.isnumeric() else x, variables_to_calculate))
        if len(variables_to_calculate) != 3:
            raise FormulaError
        if variables_to_calculate[1] not in ["/", "+", "*"]:
            raise WrongOperatorError
        if not isinstance(variables_to_calculate[0], int) or not isinstance(variables_to_calculate[2], int):
            raise ValueError
        retry = input("Бажаєте спробувати ще раз? (так/ні): ").lower()
        if retry != 'так':
            break
        break
    except FormulaError as e:
        print(e)
        print("Формула должна состоять из 3 операндов")
        print("-" * 50)
    except WrongOperatorError as e:
        print(e)
        print("Недопустимый оператор для выражения , должен быть один из (/,+,-,*) ")
        print("-" * 50)
    except ValueError as e:
        print(e)
        print("Введённые данные должны числами без точек ")
        print("-" * 50)
    except Exception as e:
        print(e)
        print("Ошибка выполения, возможно вы ввели пустую строку")
        print("-" * 50)
    finally:
        print(
            f"Вы ввели данные {'со' if count_of_input % 2 == 0 else 'с'} {count_of_input} {'раз' if count_of_input % 2 == 0 else 'раза'}, из 3 попыток")
        print("-" * 50)
print(variables_to_calculate)
try:
    if len(variables_to_calculate) != 3:
        raise EmptyOperands
    firs_operand, operation, second_operand = variables_to_calculate
    if operation == "+":
        print(f"Ответ {float(firs_operand + second_operand)}")

    elif operation == "-":
        print(f"Ответ {float(firs_operand) + float(second_operand)}")
    elif operation == "*":
        print(f"Ответ {float(firs_operand) + float(second_operand)}")
    elif operation == "/":
        print(f"Ответ {float(firs_operand) + float(second_operand)}")
except EmptyOperands:
    print("Произошла ошибка операнды пустые")
except ZeroDivisionError:
    print("Нельзя делить на 0")
print("-" * 50)
