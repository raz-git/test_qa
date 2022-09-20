from data.data import Person, Color
from faker import Faker
from random import randint

faker_ru = Faker('ru_Ru')
Faker.seed()

def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_adress=faker_ru.address(),
        permanent_adress=faker_ru.address() ,
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=randint(10, 90),
        department=faker_ru.job(),
        salary=randint(2000, 20000),
        mobile=faker_ru.msisdn(),
    )

def generated_color():
    yield  Color(
        color_name=["red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )