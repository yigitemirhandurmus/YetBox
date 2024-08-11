import os
import csv

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
        global userLoggedIn
        control_nickname = input("Kullanıcı adınızı girin: ")
        control_password = input("Şifrenizi girin: ")
        with open("users.csv", "r", encoding="utf-8") as loginFile:
            reader = csv.reader(loginFile)
            credentials = list(reader)
            print(credentials)

            for i in credentials:
                if control_nickname == i[0] and control_password == i[4]:
                    user = str(i[0])
                    print(f"Başarıyla giriş yaptınız! Kullanıcı adınız: {i[0]}")
                    userLoggedIn = True
            if userLoggedIn == False:
                print("Kullanıcı bulunamadı!")
        
print("""Hoşgeldiniz.
Yapmak istediğiniz eylemi seçin:
      1. Kullanıcı girişi
      2. Yeni kullanıcı oluşturma

      q. Çıkış      
""")

while True:
    loginSelection = input("Seçiminizi yapın: ")
    if loginSelection == "1":
        userManagement.sign_up()
    if loginSelection == "2":
        userManagement.login()
    if loginSelection == "q":
        break