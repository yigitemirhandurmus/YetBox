import os
import csv
import random

with open("films.csv", "r", encoding="cp1252") as file:
    reader = csv.reader(file, delimiter=',')
    lines = list(reader)

print("""
YetBox'a Hoşgeldiniz!

1. Bana rastgele bir film öner

a. Veritabanındaki filmleri listele
b. Veritabanına film ekle
      
Çıkmak için q tuşuna basın.
      """)

class yetbox():
    
    def randomFilm():
        randomSelection = random.choice(lines[1:])
        print(f"""
İsim: {randomSelection[0]}
Tür: {randomSelection[1]}
Çıkış Tarihi: {randomSelection[2]}
Süre (dk): {randomSelection[3]}
IMDB Puanı: {randomSelection[4]}
Dil: {randomSelection[5]}
              """)
        
    def listFilms():
        print("""
Filmler aşağıdaki şekilde listelenir:

Film numarası: "İsim", "Tür", "Çıkış Tarihi", "Süre (dk)", "IMDB Puanı", "Dil"
              """)
        for index, i in enumerate(lines[1:], start=1):
            print(f"{index}: \"{i[0]}\", \"{i[1]}\", \"{i[2]}\", \"{i[3]}\", \"{i[4]}\", \"{i[5]}\"")

    def addFilms():
        with open("films.csv", "a", encoding="cp1252") as file2:
            i = 1
            while True:
                title = str(input(f"{i}. filmin adını girin (Çıkmak için sadece Enter tuşuna basın): "))
                if title == "":
                    break
                genre = str(input(f"{i}. filmin türünü girin: "))
                premiere = str(input(f"{i}. filmin çıkış tarihini girin (ör. January 1, 2001 formatında): "))
                runtime = int(input(f"{i}. filmin süresini (dk) girin: "))
                puan = float(input(f"{i}. filmin puanını girin: "))
                language = str(input(f"{i}. filmin dilini girin: "))
                file2.write(f"{title},{genre},\"{premiere}\",{runtime},{puan},{language}\n") # Turns out using backslash before quotation marks do wonders lol
                i += 1

while True:
    userSelection = input("Seçiminizi yapın: ")
    if userSelection == "1":
        yetbox.randomFilm()
    elif userSelection.lower() == "a":
        yetbox.listFilms()
    elif userSelection.lower() == "b":
        yetbox.addFilms()
    elif userSelection.lower() == "q":
        break