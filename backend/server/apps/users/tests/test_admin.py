import pytest
from django.urls import reverse_lazy


@pytest.mark.django_db
def test_custom_user_admin(admin_client):
    resp = admin_client.get(reverse_lazy('admin:users_customuser_changelist'))
    assert resp.status_code == 200
