from django.db import models
from django.utils.translation import gettext_lazy as _

from courses.models import Classroom
from students.models import Student


class Enrollment(models.Model):
    """
    Enrollment table
    """

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pendiente'
        ENROLLMENT = 'enrollment', 'Matriculado'
        CANCELATED = 'cancelated', 'Cancelado'

    external_reference = models.CharField(
        _('Código Externo'), max_length=120, unique=True)
    internal_reference = models.CharField(
        _('Código Interno'), max_length=120, unique=True)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='enrollment', related_query_name='enrollment')
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE,
        related_name='enrollment', related_query_name='enrollment')
    status = models.CharField(
        _('Estado de Matrícula'), max_length=20, choices=Status.choices
    )
    payment_information = models.TextField(_('Información de pago'))
    create_date = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)

    class Meta:
        verbose_name = _("Matrícula")
        verbose_name_plural = _("Matrículas")

    def __str__(self) -> str:
        return f'{self.external_reference}- {self.classroom} - {self.student.name}'
