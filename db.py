filer = open('baza.txt', 'r')
filew = open('baza.txt', 'w')
class b():
    global file
    def add(h1, h2):
        x = str(h1)+"#"+str(h2)+"\n"
        filew.write(x)
        filew.close()
        return
    def read(h1):
        x = (filer.read()).split('\n')
        info = ''
        for i in range (len(x)):
            if str(h1) in x[i]:
                info += str(x[i])
        return info
b.add('pc', 'ui')
print(b.read('pc'))
