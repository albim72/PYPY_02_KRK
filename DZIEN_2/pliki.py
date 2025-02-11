from pathlib import Path
from datetime import datetime
import os
import shutil

#tworzenie katalogu
katalog = Path("moj_katalog")
katalog.mkdir(parents=True,exist_ok=True)

#tworzenie pliku i zapis daty
plik = katalog/"data.txt"
teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with plik.open("w",encoding="utf-8") as f:
    f.write(f"Aktualna data i godzina: {teraz}\n")

#uzyskiwanie listy plików w katalogu
files = os.listdir(katalog)
print(f"pliki z katalogu moj_katalog: {files}")

#sprawdzanie czy plik istnieje
if plik.exists():
    print("plik istnieje!")

#kopiowanie pliku
kopia = katalog/"kopia_danych.txt"
shutil.copy(plik,kopia)
print("plik skopiowano")

#usunięcie pliku
kopia.unlink()
print("skopiowany plik usunięty!")

#usunięcie katalogu
shutil.rmtree(katalog)
print("Katalog usunięty!")
