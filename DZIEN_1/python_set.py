drzewa = {"dąb","sosna","klon","brzoza","topola","jesion","dąb"}

print(drzewa)
print(type(drzewa))
print(drzewa)
print(drzewa)

drzewa.add("modrzew")
print(drzewa)
print(len(drzewa))

drzewa.remove("sosna")
print(drzewa)

drzewa.discard("jałowiec")
print(drzewa)

nb = [4,2,6,2,6,8,9,0,4,3,5,2,5,6,8,4,6,7]
nb = list(set(nb))
print(nb)

print("dąb" in drzewa)

inne = ("jodła","kasztan","buk")
drzewa.update(inne)
print(drzewa)

zb = {"buk","jałowiec","dąb","klon"}

print(drzewa & zb)
print(drzewa - zb)
print(drzewa^zb)

frozen_drzewa = frozenset(drzewa)
print(frozen_drzewa)
print(type(frozen_drzewa))
