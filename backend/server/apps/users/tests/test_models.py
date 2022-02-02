import pytest

from users.models import CustomUser


@pytest.mark.django_db
def test_custom_user_factory(custom_user_factory):
    user = custom_user_factory()
    # TODO: Validar image
    assert user.username is not None
    assert user.email is not None
    assert user.first_name is not None
    assert user.last_name is not None
    assert user.maternal_last_name is not None
    assert user.document_number is not None
    assert user.cellphone is not None
    assert user.phone is not None  # TODO: Optional
    assert user.sex in CustomUser.sex_options()
    assert user.address is not None  # TODO: Optional
    assert user.check_password('johnpassword')
    assert user.__str__() == user.username
    assert user.full_name == f'{user.first_name} {user.last_name}'
    assert user.user_role is not None
