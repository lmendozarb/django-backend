from django.http import HttpRequest
from django.test import TestCase
from django.utils import timezone

from faker import Faker
from users.factories import CustomUserFactory
from users.forms import CustomUserChangeForm

faker = Faker('es_ES')


class TestCustomUserChangeForm(TestCase):
    def setUp(self):
        custom_user = CustomUserFactory()
        self.req = HttpRequest()
        self.req.POST['first_name'] = custom_user.first_name
        self.req.POST['last_name'] = custom_user.last_name
        self.req.POST['maternal_last_name'] = custom_user.maternal_last_name
        self.req.POST['email'] = custom_user.email
        self.req.POST['username'] = faker.profile(fields=['username'])['username']
        self.req.POST['password'] = custom_user.password
        self.req.POST['sex'] = custom_user.sex
        self.req.POST['cellphone'] = custom_user.cellphone
        self.req.POST['date_joined'] = timezone.now()
        self.req.POST['document_number'] = faker.numerify(text='#########')

    def test_empty_form(self):
        form = CustomUserChangeForm()
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'sex']
        for field in fields:
            self.assertIn(field, form.fields)

    def test_form_ok(self):
        form = CustomUserChangeForm(self.req.POST)
        self.assertTrue(form.is_valid())
