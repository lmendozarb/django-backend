from rest_framework import serializers

from courses.models import (
    Category,
    Classroom,
    Course,
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["name"]
        read_only = True
        editable = False


class ClassroomSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False, read_only=True)

    class Meta:
        model = Classroom
        fields = [
            "internal_reference",
            "available_vacancie",
            "start_hour",
            "end_hour",
            "course",
            "qty_session",
        ]
        read_only = True


class SingleCourseSerializer(serializers.HyperlinkedModelSerializer):
    course = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = [
            "internal_reference",
            "max_vacancies",
            "start_hour",
            "end_hour",
            "qty_session",
            "is_active",
            "course"
        ]
