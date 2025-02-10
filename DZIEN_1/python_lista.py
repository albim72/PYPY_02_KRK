#lista w pythonie
kraje = ["Polska","Szwecja","Słowacja","Niemcy","Hiszpania","Irlandia"]
print(kraje)
print(type(kraje))

print(kraje[1])
print(kraje[1:3])
print(kraje[:4])
print(kraje[2:])
print(kraje[-1])
# print(kraje[-12])
print(kraje[-12:3])

print(kraje[2:6:2])
kraje.append("Włochy")
print(kraje)

kraje.insert(1,"Litwa")
print(kraje)

kraje.sort()
print(kraje)

kraje.remove("Niemcy")
kraje.insert(0,"Niemcy")

print(kraje)

s = "lajkonik"
print(s)
print(type(s))
print(s[0])
print(s[:3])

odwr = s[::-1]
print(odwr)
print(s[::2])
print(s[1::2])

print(kraje[0:][0])

sklepzoo = [[["buldog angielski","Bullterier","York"],"kot","papuga"],[[7500,7000,3500],2500,900]]
print(sklepzoo[0][0][0],"-",sklepzoo[1][0][0])

liczby = [4,6,3]
drugie = [-1,-60,45]

liczby += drugie
print(liczby)

liczby += [101]
print(liczby)
