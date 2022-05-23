import json

base_url = "http://127.0.0.1:4449"
url = "http://127.0.0.1:4449/login"

main_name = "Nikita"
main_surname = "Ведерников"
main_middle_name = "Alex"
main_username = "Retroweaver"
main_email = "test@gmail.com"
main_password = "322"


def cred_user(name, surname, middle_name, username, password, email):
    create_user = json.dumps({
        "name": f"{name}",
        "surname": f"{surname}",
        "middle_name": f"{middle_name}",
        "username": f"{username}",
        "password": f"{password}",
        "email": f"{email}"
    })
    return create_user


flask = "https://flask.palletsprojects.com/en/1.1.x/#"
cent_os = "https://www.centos.org/download/"
wire_news = "https://www.wireshark.org/news/"
wiki_api = "https://en.wikipedia.org/wiki/API"
future = "https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/"
smtp = "https://en.wikipedia.org/wiki/SMTP"
