from faker import Faker


class User:
    fake = Faker()
    email = fake.email()
    password = fake.password(special_chars=False)
    name = fake.name()


class Urls:
    url = 'https://stellarburgers.nomoreparties.site/'
