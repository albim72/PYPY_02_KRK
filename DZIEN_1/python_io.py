import os
import shutil

#CTRL+D    duplikowanie linii/bloku
#CTRL + /   komentowanie - odkomentowanie
f = open("dane.txt","r",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
print(f.closed)

print("_"*50)
f = open("dane.txt","r",encoding="utf-8")
print(f.read())

print("_"*50)
g = open("message.txt","w",encoding="utf-8")
g.write("to jest ważna wiadomość\n")
g.close()

# print("_"*50)
# g = open("message.txt","w",encoding="utf-8")
# g.write("to jest druga ważna wiadomość\n")

print("_"*50)
h = open("abc/msg.txt","a",encoding="utf-8")
h.write("to jest ważna wiadomość\n")
h.close()

sciezka = "./abc"
if os.path.exists(sciezka):
    shutil.rmtree(sciezka)
    print("katalog za danymi usunięty")
else:
    print("nie ma takiego katalogu!")
