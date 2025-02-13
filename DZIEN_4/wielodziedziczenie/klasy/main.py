from klasy.klasaa import KlasaA
from klasy.klasab import KlasaB
from klasy.klasac import KlasaC

class Trio(KlasaA,KlasaB,KlasaC):
    def __init__(self, x, y, z, msg, factor):
        KlasaA.__init__(self,x, y)
        KlasaB.__init__(self,z)
        KlasaC.__init__(self,msg)
        self.factor = factor

    def policz(self):
        return (self.x+self.z)*self.y - self.factor


t1 = Trio(4,7,2,"opis klasy...",0.3)
print(t1.policz())
print(t1.suma())
print(t1.multi())
print(t1.dziel(7))
print(t1.dziel(0))
t1.info()
