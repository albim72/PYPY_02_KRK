from ipojazd import IPojazd

class Pojazd(IPojazd):
    def __init__(self,marka,model,rodzaj_silnika):
        self.marka = marka
        self.model = model
        self.rodzaj_silnika = rodzaj_silnika
        
    def __repr__(self):
        return f'samochód {self.marka} {self.model}\nrodzaj silnika -> {self.rodzaj_silnika}'
    
