adress=input().split(".")
print(True if len(adress) == 4 and all(0 <= int(i) <= 255 for i in adress )  else False)