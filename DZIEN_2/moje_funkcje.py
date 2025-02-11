def hej():
    return print("Jak mija dzień?")

hej()
hej()
h = hej()
print(h)

n=100
def dodaj(a,b,d,c=1):
    global n
    n = a+b+2*c-d+n
    return n

print(dodaj(4,7,3))
print(dodaj(4,7,2))
print(dodaj(4,7,False))
print(n)

#funkcja z arbitralną liczbą argumentów
def pomnoz(*args):
    wynik=1
    for num in args:
        wynik*=num

    return wynik

print(pomnoz(2,5))
print(pomnoz(2,5,1,78))
print(pomnoz(2,5,1,2,7,8,4,6,1))
print(pomnoz())

for i in range(21):
    wynik = i*8

print(wynik)
