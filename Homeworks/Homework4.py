# 1)
names = ["john", "marta", "james", "amanda", "marianna"]
names=list(map(lambda x : str(x).title(),names))
names = " ".join(names)
print(names)

# 2)
names = ["FirstItem", "FriendsList", "MyTuple"]
names = [list(i) for i in names]
for key in range(len(names)):
    for value in range(1, len(names[key])):
        if names[key][value].istitle():
            names[key][value] = "_" + names[key][value].lower()
    names[key] = "".join(names[key]).lower()
print(names)
names = ["FirstItem", "FriendsList", "MyTuple"]
names = [name[0].lower() + ''.join(['_' + char.lower() if char.istitle() else char for char in name[1:]]) for name in names]
print(names)
# 3
programming_languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

for language, author in programming_languages.items():
    print(f"My favorite programming language is {language}. It was created by {author}.")

del programming_languages["C++"]

# 4
casino_blacklist = {"John Dow", "Alice Smith", "Bob Johnson", "Mary White"}
poker_blacklist = {"John Dow", "Bob Johnson", "Eve Brown"}
alcohol_blacklist = {"John Dow", "Mary White", "Eve Brown", "Michael Davis"}

casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(casino_blacklist)

# 5

names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for name in names:
    if not isinstance(name, str) or name is None:
        continue
    print(name)

# 6
string_to_change = input("Введите строку:")

result = {}
for key in string_to_change:
    result[key] = result.get(key, 0) + 1
for key, value in result.items():
    print(f"{key},{value} ", end="")
