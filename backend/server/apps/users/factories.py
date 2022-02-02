import factory
from faker import Faker
from users.models import CustomUser

faker = Faker('es_ES')


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = faker.profile(fields=['username'])['username']
    first_name = faker.first_name()
    last_name = faker.last_name()
    maternal_last_name = faker.last_name()
    document_number = faker.numerify(text='#########')
    cellphone = faker.numerify(text='+56#########')
    phone = faker.numerify(text='+56#########')
    sex = faker.random_element(elements=CustomUser.sex_options())
    email = faker.email()
    address = faker.address()
    password = factory.PostGenerationMethodCall('set_password', 'johnpassword')
