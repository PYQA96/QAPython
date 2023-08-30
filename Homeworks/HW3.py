



def Is_polindrom(name : str):
    if name.lower() == name[::-1].lower():
        return f"+"
    else:
        return f"-"


word=input("Введите слово: ")
print(Is_polindrom(word))
print("-" * 50)

def Search_the_word(name : str, search_word : str):
    name=name.lower().split()
    if search_word in name:
        print("-" * 50)
        return f"Yes"
    else:
        print("-" * 50)
        return f"No"


print("-"*50)
word=input("Введите фразу: ")
word_serch=input("Введите слово для описка: ")
print(Search_the_word(word,word_serch))


def Convert_to_strinf(word : str):
    word=word.split()
    if len(word)<3:
        return f"Длиина списка {len(word)} меньше чем 3 элемента"
    return f"Длиина списка {len(word)}"


word=input("Введите слово: ")
print(Is_polindrom(word))
print("-" * 50)



def Valid_ip_adress(adres : str):
    adres=adres.split(".")
    adres=[ int(num) for num in adres if num.isdigit() and 0 <= int(num) <= 255 ]
    if len(adres)<4:
        return f"Адресс почты не валидный, такго адреса не существует"
    else:
        return f"Адресс почты  валидный, адрес  существует"





word="244.123.12.1"
print(Valid_ip_adress(word))
print("-" * 50)
a="244.123.12.1"
print(a.split("."))





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

ip_address = input("Введіть IP-адресу: ")
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