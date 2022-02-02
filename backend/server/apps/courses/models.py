from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from core.models import TimestampMixin

# Create your models here.

class Category(MPTTModel):
    """
    Category table implimented with MPTT
    """

    name = models.CharField(_("Nombre"), max_length=100,
        help_text=_("format: required, max-100"),
    )
    slug = models.SlugField(_("URL segura de categoria"),
        max_length=150,
        help_text=_("format: required, letters, numbers, underscore, or hyphens"),
    )
    is_active = models.BooleanField(default=True)

    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Categoria")
        verbose_name_plural = _("Categorias")

    def __str__(self) -> str:
        return self.name


class Course(TimestampMixin):
    """
    Course table
    """

    internal_reference = models.CharField(_('Código Interno'), max_length=120, unique=True)
    name = models.CharField(_('Nombre'), max_length=255)
    description = models.TextField(_('Descripción'))
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(_("Curso Disponible"),
        help_text=_("format: true=product visible"),
    )

    class Meta:
        verbose_name = _("Curso")
        verbose_name_plural = _("Cursos")

    def __str__(self) -> str:
        return f'{self.name}- {self.internal_reference}'


class Classroom(TimestampMixin):
    """
    Classroom table
    """

    internal_reference = models.CharField(_('Código Interno'), max_length=120, unique=True)
    available_vacancie = models.IntegerField(_('Vacantes disponibles'), default=0)
    max_vacancies = models.IntegerField(_('Vacantes Máximas'), default=0)
    student_enrollment = models.IntegerField(_('Alumnos Matriculados'), default=0)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='classroom', related_query_name='classroom')
    start_hour = models.CharField(_('Hora de Inicio'), max_length=15)
    end_hour = models.CharField(_('Hora de Fin'), max_length=15)
    qty_session = models.IntegerField(_('Cantidad de Sesiones'), default=0)
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Classroom Disponible")
    )

    class Meta:
        verbose_name = _("Clase")
        verbose_name_plural = _("Clases")

    def __str__(self) -> str:
        return f'{self.internal_reference} - {self.course}'
