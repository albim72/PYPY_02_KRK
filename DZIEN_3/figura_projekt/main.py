from figury.prostokat import Prostokat
from figury.trojkat import Trojkat
from figury.trapez import Trapez
from figury.kolo import Kolo


tr = Trojkat(5.6,7.2)
print(f'pole figury {tr.__class__.__name__} wynosi: {tr.policz_pole():.2f} cm2')

pr = Prostokat(4.4,6.7)
print(f'pole figury {pr.__class__.__name__} wynosi: {pr.policz_pole():.2f} cm2')

kw = Prostokat(5.1,5.1)
print(f'pole figury {kw.__class__.__name__} wynosi: {kw.policz_pole():.2f} cm2')

trp = Trapez(3.7,5.8,4.4)
print(f'pole figury {trp.__class__.__name__} wynosi: {trp.policz_pole():.2f} cm2')

kl = Kolo(5.5)
print(f'pole figury {kl.__class__.__name__} wynosi: {kl.policz_pole():.2f} cm2')
