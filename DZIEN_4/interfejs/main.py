from pojazd import Pojazd

p1 = Pojazd("Opel","Insignia","diesel")
print(p1)

odl = 567
jedn = 47
cj = 6.23

print(f"spalanie l/100km: {p1.spalanie(odl,jedn):.2f}")
print(f"koszt przejazdu na trasie {odl} km wynosi {p1.kosztyprzejazdu(odl,jedn,cj):.2f} zł")
