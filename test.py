def sign_up():
    global user_name
    global user_surname
    global user_gmail
    global user_password
    global user_password_again
    global nickname
    user_name = input("Name ")
    user_surname = input("Surname ")
    user_gmail = input("Gmail ")
    nickname = input("Nickname ")
    user_password = input("Password (0-9,a-z,A-Z,special characters) ")
    user_password_again = input("Password (0-9,a-z,A-Z,special characters) ")
    if user_password_again == user_password:
        return ("Hesabınız oluşturuldu.")
    else:
        print("Şifreleriniz uyumsuz!")
        while True:
            user_password_again = input("Password (0-9,a-z,A-Z,special characters) ")
            if user_password_again == user_password:
                print("Hesabınız oluşturuldu.")
                break
sign_up()

def login():
    control_nickname = input("Nickname ")
    control_password = input("Password (0-9,a-z,A-Z,special characters) ")
    if control_password != user_password:
        for entry in range(5):
            control_password = input("Password (0-9,a-z,A-Z,special characters) ")
            if control_password == user_password:
                print("Başarıyla giriş yapıldı.")
                break
            else:
                print(f"{4 - entry} giriş hakkın kaldı!")
    else:
        return ("Başarıyla giriş yapıldı.")
login()