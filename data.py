from faker import Faker

fake = Faker()

email = fake.email()
password = fake.password(special_chars=False)
name = fake.name()
url = 'https://stellarburgers.nomoreparties.site/'
