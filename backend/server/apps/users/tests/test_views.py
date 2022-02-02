import pytest
from rest_framework import status
from rest_framework.test import APITestCase

from pytest_factoryboy import register
from users.factories import CustomUserFactory

register(CustomUserFactory)


@pytest.mark.django_db
class TestCustomUserViewSet(APITestCase):

    endpoint = '/api/v1/users/users/'
    token_url = '/api/v1/users/token/'

    def test_retrieve_without_login(self):
        user = CustomUserFactory()
        url = f'{self.endpoint}{user.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_with_login(self):
        user = CustomUserFactory()
        resp = self.client.post(
            self.token_url,
            {'username': user.username, 'password': 'johnpassword'},
            format='json',
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn('access', resp.data)
        token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = f'{self.endpoint}{user.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUserAndToken(APITestCase):

    token_url = '/api/v1/users/token/'

    def _create_user_and_token(self):
        user = CustomUserFactory()
        resp = self.client.post(
            self.token_url,
            {'username': user.username, 'password': 'johnpassword'},
            format='json',
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn('access', resp.data)
        token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
