import os
import csv
import random

with open("films.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    lines = list(reader)

print("""
YetBox'a Hoşgeldiniz!

1. Bana rastgele bir film öner

a. Veritabanındaki filmleri listele
b. Veritabanına film ekle
c. Veritabanından film sil
      
Çıkmak için q tuşuna basın.
      """)

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Hata: Lütfen geçerli bir tam sayı girin.")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.")

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
        with open("films.csv", "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            i = 1
            while True:
                try:
                    title = input(f"{i}. filmin adını girin (Çıkmak için sadece Enter tuşuna basın): ")
                    if title == "":
                        break
                    genre = input(f"{i}. filmin türünü girin: ")
                    premiere = input(f"{i}. filmin çıkış tarihini girin (ör. January 1, 2001 formatında): ")
                    runtime = get_int_input(f"{i}. filmin süresini (dk) girin: ")
                    score = get_float_input(f"{i}. filmin puanını girin: ")
                    language = input(f"{i}. filmin dilini girin: ")
                    
                    writer.writerow([title, genre, premiere, runtime, score, language])
                    i += 1
                except Exception as e:
                    print(f"{e}. Lütfen tekrar deneyin.")

    def delFilms():
        with open('films.csv', "r", newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            delLines = list(reader)[1:]

        total_films = len(delLines)
        print(f"Toplam {total_films} film var.")

        try:
            to_delete = int(input("Silmek istediğiniz filmin numarasını girin: "))
            if 1 <= to_delete <= total_films:
                delete_index = to_delete - 1
                del delLines[delete_index]
                with open('films.csv', 'w', newline='', encoding="utf-8") as csvfile:
                    csvfile.write("Title,Genre,Premiere,Runtime,IMDB Score,Language\n")
                    writer = csv.writer(csvfile)
                    writer.writerows(delLines)
                    print(f"{to_delete}. film başarıyla silindi.")
            else:    
                print(f"Lütfen 1 ile {total_films} arasında bir sayı girin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")


while True:
    userSelection = input("Seçiminizi yapın: ")
    if userSelection == "1":
        yetbox.randomFilm()
    elif userSelection.lower() == "a":
        yetbox.listFilms()
    elif userSelection.lower() == "b":
        yetbox.addFilms()
    elif userSelection.lower() == "c":
        yetbox.delFilms()
    elif userSelection.lower() == "q":
        break

