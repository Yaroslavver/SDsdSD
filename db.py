def add(tip, model, info):
    file = open('baza.txt', 'a+')
    x = str(tip)+"#"+str(model)+"#"+str(info)+"\n"
    file.write(x)
    file.close()
    return
while True:
    c = input("Введите команду: ")
    if c == "add":
        a1 = input("___Тип устройства: ")
        a2 = input("___Модель или разработчик: ")
        a3 = input("___Характеристика: ")
        add(a1, a2, a3)
        print("_____Устройство успешно добавлено")
