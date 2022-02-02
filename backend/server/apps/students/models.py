from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimestampMixin


# Create your models here.
class Student(TimestampMixin):
    class Sex(models.TextChoices):
        MAN = 'M', 'Masculino'
        WOMAN = 'F', 'Femenino'

    internal_reference = models.CharField(_('Código Interno'), max_length=255)
    name = models.CharField(_('Nombres'), max_length=255)
    lastname = models.CharField(_('Apellidos'), max_length=255)
    birth_date = models.DateTimeField(_('Fecha de Nacimiento'))
    sex = models.CharField(_('Sexo'), max_length=1, choices=Sex.choices)
    image = models.ImageField(_('Imagen'), upload_to='students/')
    address = models.CharField(_('Dirección'), max_length=250)
    college = models.CharField(_('Colegio'), max_length=180)
    nationality = models.CharField(_('Nacionalidad'), max_length=100)
    qty_brother = models.IntegerField(_('Número de Hermanos'), default=0)
    age = models.IntegerField(_('Edad'), default=1)

    def __str__(self) -> str:
        return f'{self.name} {self.lastname} - {self.age}'

    class Meta:
        verbose_name = _('Estudiante')
        verbose_name_plural = _('Estudiantes')


class ParentStudent(TimestampMixin):
    class DocumentType(models.TextChoices):
        RUC = 'RUC', 'RUC'
        DNI = 'DNI', 'DNI'
        PPT = 'PPT', 'PPT'

    name = models.CharField(_('Nombres'), max_length=255)
    lastname = models.CharField(_('Apellidos'), max_length=255)
    birth_date = models.DateTimeField(_('Fecha de Nacimiento'))
    email = models.EmailField(_('Correo Electronico'), max_length=200)
    phone = models.CharField(_('Teléfono Movil'), max_length=25)
    occupation = models.CharField(_('Ocupación'), max_length=80)
    document_type = models.CharField(
        _('Tipo de documento'),
        max_length=5,
        choices=DocumentType.choices,
        default='DNI',
    )
    document_number = models.CharField(_('Número de documento'), max_length=20)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='parent_student', related_query_name='parent_student')

    def __str__(self) -> str:
        return f'{self.name} {self.lastname} \\-> {self.student.name} \
            {self.student.internal_reference}'

    class Meta:
        verbose_name = _('Apoderado')
        verbose_name_plural = _('Apoderados')
