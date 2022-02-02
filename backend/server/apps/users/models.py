from django.contrib.auth.models import (
    AbstractUser,
    Group,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(Group):
    # TODO: Add through model
    class Meta:
        proxy = True
        verbose_name = _('Rol')
        verbose_name_plural = _('Roles')


class CustomUser(AbstractUser):
    class Sex(models.TextChoices):
        MAN = 'M', 'Masculino'
        WOMAN = 'F', 'Femenino'

    maternal_last_name = models.CharField(_('Apellido Materno'), max_length=70)
    document_number = models.CharField(_('RUT'), max_length=12)
    cellphone = models.CharField(_('Número de celular'), max_length=15)
    phone = models.CharField(_('Número de casa'), max_length=15, blank=True, null=True)
    sex = models.CharField(_('Sexo'), max_length=1, choices=Sex.choices)
    address = models.CharField(_('Dirección'), max_length=120, blank=True, null=True)

    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
        'maternal_last_name',
        'document_number',
        'cellphone',
    ]

    @classmethod
    def sex_options(cls):
        return [option[0] for option in cls.Sex.choices]

    def add_groups(self, groups_id):
        for group_id in groups_id:
            self.groups.add(group_id)

    def remove_groups(self, groups_id):
        for group_id in groups_id:
            self.groups.remove(group_id)

    def add_permissions(self, permissions_id):
        for permission_id in permissions_id:
            self.user_permissions.add(permission_id)

    def remove_permissions(self, permissions_id):
        for permission_id in permissions_id:
            self.user_permissions.remove(permission_id)

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def user_role(self):
        if self.is_superuser:
            return _('Administrador')
        if self.is_staff:
            return _('Moderador')
        return _('Usuario')
