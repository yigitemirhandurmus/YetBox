import os
import csv
import random
import json
from datetime import datetime

if not os.path.exists("users.csv"):
    with open("users.csv", "w", encoding="utf-8") as loginFile:
        pass

userLoggedIn = False
class userManagement():
    def sign_up():
        global user_name
        global user_surname
        global user_email
        global user_password
        global user_password_again
        global nickname
        user_name = input("İsim: ")
        user_surname = input("Soyisim: ")
        user_email = input("E-mail: ")
        nickname = input("Kullanıcı adı: ")
        user_password = input("Şifre: ")
        user_password_again = input("Şifrenizi tekrar girin: ")
        if user_password_again == user_password:
            with open("users.csv", "a", encoding="utf-8") as loginFile:
                writer = csv.writer(loginFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([nickname, user_name, user_surname, user_email, user_password])
            print("Hesabınız oluşturuldu.")
        else:
            print("Şifreleriniz uyumsuz! Tekrar deneyin.")

    def login():
        global user
        global userLoggedIn
        control_nickname = input("Kullanıcı adınızı girin: ")
        control_password = input("Şifrenizi girin: ")
        with open("users.csv", "r", encoding="utf-8") as loginFile:
            reader = csv.reader(loginFile)
            credentials = list(reader)

            for i in credentials:
                if control_nickname == i[0] and control_password == i[4]:
                    user = str(i[0])
                    print(f"Başarıyla giriş yaptınız! Kullanıcı adınız: {i[0]}")
                    userLoggedIn = True
            if userLoggedIn == False:
                print("Kullanıcı bulunamadı!")

    def assignIDs():
        filename = 'assign_id.py'
        with open(filename) as script:
            exec(script.read())

print("""Hoşgeldiniz.
Yapmak istediğiniz eylemi seçin:
      1. Yeni kullanıcı oluşturma
      2. Kullanıcı girişi

      i. Film veritabanındaki her filme bir ID ata (sadece debugging için kullanın!)

      q. Çıkış      
""")
if userLoggedIn == False:
    while True:
        loginSelection = input("Seçiminizi yapın: ")
        if loginSelection.lower() == "1":
            userManagement.sign_up()
            break
        elif loginSelection.lower() == "2":
            userManagement.login()
            break
        elif loginSelection.lower() == "i":
            userManagement.assignIDs()
            print("İşlem gerçekleştirildi.")
            break
        elif loginSelection.lower() == "q":
            break

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

    class Comments():
        global load_films
        global load_comments
        global save_comment
        global add_comment

        def load_films():
            films = {}
            with open("films.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    films[row['Title']] = row['ID']
            return films

        def load_comments():
            try:
                with open("comments.json", 'r') as file:
                    return json.load(file)
            except FileNotFoundError:
                return {}

        def save_comment(comments):
            with open("comments.json", 'w') as file:
                json.dump(comments, file, indent=2)

        def add_comment(films, comments):
            film_title = input("Yorum eklemek istediğiniz filmin adını girin: ")
            if film_title not in films:
                print("Film bulunamadı.")
                return

            film_id = films[film_title]
            username = user
            comment_text = input("Yorumunuzu girin: ")
            timestamp = datetime.now().isoformat()

            if film_id not in comments:
                comments[film_id] = []

            comments[film_id].append({
                "username": username,
                "comment": comment_text,
                "timestamp": timestamp
            })

            save_comment(comments)
            print("Yorum başarıyla eklendi!")

        def main():
            films = load_films()
            comments = load_comments()

            while True:
                add_comment(films, comments)
                if input("Başka bir film eklemek ister misiniz? (Evet için e tuşuna basın, hayır için diğer herhangi bir tuşa basın): ").lower() != 'e':
                    break

if userLoggedIn == True:
    with open("films.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=',')
        lines = list(reader)

    print("""
    YetBox'a Hoşgeldiniz!

    1. Bana rastgele bir film öner
    2. Seçtiğim bir filme yorum yap

    a. Veritabanındaki filmleri listele
    b. Veritabanına film ekle
    c. Veritabanından film sil
        
    Çıkmak için q tuşuna basın.
        """)

    while True:
        userSelection = input("Seçiminizi yapın: ")
        if userSelection == "1":
            yetbox.randomFilm()
        elif userSelection.lower() == "2":
            yetbox.Comments.main()
        elif userSelection.lower() == "a":
            yetbox.listFilms()
        elif userSelection.lower() == "b":
            yetbox.addFilms()
        elif userSelection.lower() == "c":
            yetbox.delFilms()
        elif userSelection.lower() == "q":
            break
else:
    print("Henüz giriş yapmadınız! Giriş yapabilmek ve seçenekleri görebilmek için programı tekrar çalıştırın.")

