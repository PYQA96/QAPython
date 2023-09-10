str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
result1 = {}
result2 = {}
result3 = {}
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
for list1, list2 in zip(str_list, square_list):
    result3[list1] = list2
print(result3)


# калькулятор

class EmptyOperand(Exception):
    pass


class FormulaError(Exception):
    pass


class WrongOperatorError(Exception):
    pass


class FormulaError(Exception):
    pass


def calculate(formula):
    try:
        if len(formula) != 3:
            raise FormulaError("Неверное количество операндов")

        num1, operator, num2 = formula

        if not (num1.isnumeric() and num2.isnumeric()):
            raise FormulaError("Числа должны быть целыми")

        num1 = float(num1)
        num2 = float(num2)

        if operator not in ('*', '/'):
            raise FormulaError("Неверный оператор, используйте '*' или '/'.")

        if operator == '/' and num2 == 0:
            raise FormulaError("Деление на ноль запрещено")

        if operator == '*':
            result = num1 * num2
        else:
            result = num1 / num2

        return result

    except Exception as e:
        raise FormulaError(f"Ошибка ввода: {e}")


attempts = 3
for counts in range(attempts):
    formula = input("Введите формулу (например, 2 * 5): ")
    try:
        formula = formula.split()
        result = calculate(formula)
        print(f"Результат: {result}")
    except FormulaError as e:
        print(f"Ошибка: {e}")
    if counts == 2:
        print(f"Конец програмы")
        print("_" * 50)
        break
    retry = input("Хотите попробовать еще раз? (да/нет): ").lower()
    if retry != 'да':
        print(f"Конец програмы")
        print("_" * 50)
        break

# оптимизировал все как мог , сократил код и сделал множественную обработку исключений
count_of_input = 0
variables_to_calculate = None
firs_operand, operation, second_operand = None, None, None
while count_of_input < 3:
    try:
        count_of_input += 1
        variables_to_calculate = input("Введите данные в формате (число,выражение,число) через пробел: ").split()
        variables_to_calculate = list(map(lambda x: int(x) if x.isnumeric() else x, variables_to_calculate))
        if len(variables_to_calculate) != 3:
            raise FormulaError("Формула должна состоять из 3 операндов")
        elif variables_to_calculate[1] not in ["/", "+", "*" , "-"]:
            raise WrongOperatorError("Недопустимый оператор для выражения , должен быть один из (/,+,-,*) ")
        elif not isinstance(variables_to_calculate[0], int) or not isinstance(variables_to_calculate[2], int):
            raise ValueError("Введённые данные должны простыми числами ")
        firs_operand, operation, second_operand = variables_to_calculate
        if operation == "+":
            print(f"Ответ {float(firs_operand) + float(second_operand)}")
        elif operation == "-":
            print(f"Ответ {float(firs_operand) - float(second_operand)}")
        elif operation == "*":
            print(f"Ответ {float(firs_operand) * float(second_operand)}")
        elif operation == "/":
            if second_operand == 0:
                raise ZeroDivisionError("Нельзя делить на 0")
            print(f"Ответ {float(firs_operand) / float(second_operand)}")
    except (ZeroDivisionError, FormulaError, WrongOperatorError, ValueError, Exception) as e:
        print(f"Ошибка: {e}")
    else:
        if count_of_input >= 3:
            print("Попытки кончились")
            break
        else:
            retry = input("Бажаєте спробувати ще раз? (так/ні): ").lower()
            if retry.lower() != 'так':
                break
    finally:
        print("-" * 50)
        print(
            f"Вы ввели данные {'со' if count_of_input % 2 == 0 else 'с'} {count_of_input} {'раз' if count_of_input % 2 == 0 else 'раза'}, из 3 попыток")
        print("-" * 50)
