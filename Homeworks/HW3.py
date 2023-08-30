def is_palindrome(word: str):
    if word.lower() == word[::-1].lower():
        return "+"
    else:
        return "-"


input_word = input("Введите слово: ")
print(is_palindrome(input_word))
print("-" * 50)


def search_word_in_phrase(phrase: str, search_word: str):
    words = phrase.lower().split()
    if search_word in words:
        print("-" * 50)
        return "Yes"
    else:
        print("-" * 50)
        return "No"


print("-" * 50)
input_phrase = input("Введите фразу: ")
input_search_word = input("Введите слово для поиска: ")
print(search_word_in_phrase(input_phrase, input_search_word))


def check_list_length(input_string: str):
    words = input_string.split()
    if len(words) < 3:
        return f"Длина списка {len(words)} меньше 3 элементов"
    return f"Длина списка {len(words)}"


input_string = input("Введите строку: ")
print(check_list_length(input_string))
print("-" * 50)


def validate_ip_address(address: str):
    original_address = address
    components = address.split(".")
    valid_components = [num for num in components if num.isdigit() and 0 <= int(num) <= 255]
    if original_address.replace(".", "", 3) != "".join(valid_components):
        return "Неверный IP-адрес"
    else:
        return "Верный IP-адрес"


input_address = input("Введите IP-адрес: ")
print(validate_ip_address(input_address))

# без функций только по пройденым тема


word = input("Введіть слово: ")
if word == word[::-1]:
    print('+')
else:
    print('-')

text = input("Введіть текст: ")
search_word = input("Введіть слово для пошуку: ")
if search_word in text:
    print('YES')
else:
    print('NO')

email = input("Введіть пошту: ")
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')

text = input("Введіть текст через пробіл: ")
text_list = text.split()
if len(text_list) >= 3:
    print("Останні 3 елементи:", text_list[-3:])
else:
    print(f"Кількість елементів менша за 3: {len(text_list)}")

ip_address = input("Введіть слово: ")
ip_parts = ip_address.split('.')

is_valid = True
for part in ip_parts:
    if not part.isdigit() or not 0 <= int(part) <= 255:
        is_valid = False
        break

if is_valid and len(ip_parts) == 4:
    print('Коректна IP-адреса')
else:
    print('Неправильна IP-адреса')
