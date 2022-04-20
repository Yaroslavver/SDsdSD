import json
filer = open('baza.txt', 'r')
filew = open('baza.txt', 'w')
class b():
    global file
    def add(h1, h2):
        x = str(h1)+"#"+str(h2)+"\n"
        filew.write(x)
    def read(h1):
        x = (filer.read()).split('\n')
        info = ''
        for i in range (len(x)):
            if str(h1) in x[i]:
                info += str(x[i])
        return info
b.add('phone', 'Android')
b.add('phone', 'Apple')
b.add('PC', 'hp')
b.add('PC', 'acer')
b.add('PC', 'samsung')
print(b.read('phone'))
