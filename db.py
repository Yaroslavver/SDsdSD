comands = "Выберите команду: \n1 - Поиск \n2 - Добавить устройство \n3 - Вывести список устройств \nExit - Выход"
def check():
    with open("Base.txt","r") as file:
        print("Расширенный поиск: \nВведите тип устройства:",end = " ")
        type = input()
        print("Введите модель: ",end = " ")
        model = input()
        for dt in file:
            if type in dt and model in dt:
                print(dt[dt.index("#"):])


def add(tip, model, info):
    file = open('baza.txt', 'a+')
    x = str(tip)+"#"+str(model)+"#"+str(info)+"\n"
    file.write(x)
    file.close()
    return

print(comands)
comand = input()
while comand != "Exit":
    if comand == "1":
        check()
    elif comand == "2":
        a1 = input("___Тип устройства: ")
        a2 = input("___Модель или разработчик: ")
        a3 = input("___Характеристика: ")
        add(a1, a2, a3)
        print("_____Устройство успешно добавлено")

    elif comand == "3":
        with open("Base.txt","r") as file:
            for i in range(1,len(file)):
                print(file.readline())

    print(comands)
    comand = input()



# with open("Base.txt","r") as file:
#     Types = []
#     type = ""
#     for i in file.readline():
#         if i != "#":
#             type += i
#         else:
#             Types.append(type)