from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework import (
    mixins,
    viewsets,
)
from rest_framework.response import Response

from courses.models import Classroom
from courses.serializers import (
    ClassroomSerializer,
    SingleCourseSerializer,
)


# Create your views here.
@extend_schema_view(
    list=extend_schema(
        summary='List a course by category',
        description='Return a list of all courses in this category.',
        tags=['Courses'],
    ),
)
class CourseByCategory(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    """
    API endpoint that returns course by category
    """

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    def list(self, request, slug=None):
        queryset = Classroom.objects.filter(
            course__category__slug=slug,
        ).filter(is_active=True)[:10]
        serializer = ClassroomSerializer(
            queryset, context={"request": request}, many=True
        )
        return Response(serializer.data)


@extend_schema_view(
    retrieve=extend_schema(
        summary='Return single classroom',
        description='Return the classroom asociated with a specific course.',
        tags=['Courses'],
    ),
)
class SingleCourseViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    """
    API endpoint that returns courses item
    """

    queryset = Classroom.objects.all()
    serializer_class = SingleCourseSerializer
    lookup_field = "course__internal_reference"

    def retrieve(self, request, internal_reference=None):
        queryset = Classroom.objects.filter(internal_reference=internal_reference)
        serializer = SingleCourseSerializer(queryset, many=True)
        return Response(serializer.data)
