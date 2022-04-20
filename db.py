comands = "Выберите команду: \n1 - Поиск \n2 - Добавить устройство \n3 - Вывести список устройств \nExit - Выход"
# with open("Base.txt","r") as file:
#     Types = []
#     type = ""
#     for i in file.readline():
#         if i != "#":
#             type += i
#         else:
#             Types.append(type)

def check():
    with open("Base.txt","r") as file:
        print("Расширенный поиск: \nВведите тип устройства:",end = " ")
        type = input()
        print("Введите модель: ",end = " ")
        model = input()
        for dt in file:
            if type in dt and model in dt:
                print(dt[dt.index("#"):])


print(comands)
comand = input()
while comand != "Exit":
    if comand == "1":
        check()
    elif comand == "2":
        add()
    elif comand == "3":
        with open("Base.txt","r") as file:
            for i in range(1,len(file)):
                print(file.readline())

    print(comands)
