import os
import csv
import random

with open("films.csv", "r", encoding="cp1252") as file:
    reader = csv.reader(file, delimiter=',')
    lines = list(reader)

print("""
YetBox'a Hoşgeldiniz!

1. Bana rastgele bir film öner
      
Çıkmak için q tuşuna basın.
      """)

class yetbox():
    
    def randomFilm():
        randomSelection = random.choice(lines[1:])
        print(f"""
İsim: {randomSelection[0]}
Tür: {randomSelection[1]}
Çıkış Tarihi: {randomSelection[2]}
Süre: {randomSelection[3]}
IMDB Puanı: {randomSelection[4]}
Dil: {randomSelection[5]}
              """)

while True:
    userSelection = input("Seçiminizi yapın: ")
    if userSelection == "1":
        yetbox.randomFilm()
    elif userSelection.lower() == "q":
        break