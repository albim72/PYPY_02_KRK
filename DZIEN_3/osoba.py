class Osoba:
    #opis stanu
    __kolor_oczu = "niebieski"

    def __init__(self,imie,wiek,wzrost,waga):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.waga = waga
        self.kolor_oczu = f"kolor oczu: {self.__kolor_oczu}"
        print(self.msg("Nowa klasa:"))

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Osoba)
    def __repr__(self):
        return (f"Osoba -> imię: {self.imie}, wiek: {self.wiek}\n"
                f"wzrost: {self.wzrost} cm, waga: {self.waga} kg\n"
                f"_________________________________________")

    def __call__(self, x):
        return f"wiek za {x} lat: {self.wiek + x}"

    def msg(self,info):
        return f"{info} - klasa: {self.__class__.__name__}"

    def powitanie(self):
        return f"Witaj {self.imie}!"

    def getimie(self):
        return self.imie

    def setimie(self,noweimie):
        self.imie = noweimie

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self,nowywiek):
        self._wiek = nowywiek


os = Osoba("Anna",45,167,57)
os = Osoba("Hanna",45,167,57)
os2= Osoba("Henryk",23,166,60)
print(os.getimie())
os.setimie("Karol")
print(os.getimie())
print(os)
print(os2)

print(os(5))
print(os.msg("ABC"))
print(os.kolor_oczu)
print(os.powitanie())
print(os.wiek)
os.wiek = 78
print(os.wiek)









