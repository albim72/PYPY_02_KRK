def oblicz_srednia(lista_liczb):
    if not lista_liczb:
        return None
    suma = sum(lista_liczb)
    srednia = suma/len(lista_liczb)
    return srednia

def opisz_srednia(srednia,lista_liczb):
    if srednia is None:
        return "Lista jest pusta, nie można policzyć średniej!"
    return f'Średnia z liczb: {lista_liczb} wynosi: {srednia:.2f}'

liczby1 = [2,4,6,8,10]
srednia1 = oblicz_srednia(liczby1)
print(opisz_srednia(srednia1,liczby1))

liczby2 = []
srednia2 = oblicz_srednia(liczby2)
print(opisz_srednia(srednia2,liczby2))

liczby3 = [-3,0,6,-12,98,0.45,13.8,-4.5]
srednia3 = oblicz_srednia(liczby3)
print(opisz_srednia(srednia3,liczby3))

#funkcje anonimowe
print((lambda a:a+10)(19))
print((lambda a:a+10)(4.5674))

x = lambda a,b,c:a+b+c+1
print(x(5,7,3))

def multi(n):
    return lambda a:a*n

print(multi(5)(4))

nb = [4,7,2,89,3,79,3,6,11,35,88,245,0,-24,-2,-5,2]

parzyste = list(filter(lambda x:x%2==0,nb))
print(parzyste)

cube = list(map(lambda x:x**3,nb))
print(cube)

#list comprehension
ob = [x**5-12 for x in range(1,2001) if x%2==0]
print(ob)
