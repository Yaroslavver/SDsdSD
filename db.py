comands = "Выберите команду: \n1 - Поиск \n2 - Добавить устройство \n3 - Вывести список устройств \nExit - Выход"
def check():
    with open("Base.txt","r") as file:
        print("Расширенный поиск: \nВведите тип устройства:",end = "")
        type = input()
        print("Введите модель: ",end = "")
        model = input()
        flag = True
        for dt in file:
            if type.lower() in dt.lower() and model.lower() in dt.lower():
                print(dt[dt.index("#")+1:].replace("#", " | "))
                flag = False
        if flag:
            print("Не найдено")
        return


def add(tip, model, info):
    file = open('Base.txt', 'a+')
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
            print(file.read().replace("#"," | "))

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