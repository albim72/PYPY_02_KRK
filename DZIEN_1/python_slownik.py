pojazd = {
    "marka":"Ford",
    "model":"Mustang",
    "rok":2019,
    "kolor":"czarny",
    123:"pb98"
}

print(pojazd)
print(type(pojazd))

print(pojazd["model"])
print(pojazd[123])
pojazd["kolor"] = "biały"

print(pojazd)

pojazd["przebieg"] = 135600
print(pojazd)

print("_"*50)
for i in pojazd.keys():
    print(i)

print("_"*50)
for i in pojazd.values():
    print(i)

print("_"*50)
for n,k in pojazd.items():
    print(n,":",k)

miasto = {
    "Warszawa":{
        "województwo":"mazowieckie",
        "populacja":1890340,
        "poiwerzchnia":517.24
    },
    "Kraków":{
        "województwo":"małopolskie",
        "populacja":780000,
        "poiwerzchnia":326.86
    },
    "Łódź":{
        "województwo":"łódzkie",
        "populacja":670100,
        "poiwerzchnia":293.25
    },
    "Wrocław":{
        "województwo":"dolnośląskie",
        "populacja":643000,
        "poiwerzchnia":292.12
    },
    "Gdańsk":{
        "województwo":"pomorskie",
        "populacja":470900,
        "poiwerzchnia":262
    }
}

print(miasto)
print(miasto["Warszawa"])
print(miasto["Warszawa"]["województwo"])
