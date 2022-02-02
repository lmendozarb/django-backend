from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from users.models import (
    CustomUser,
    Role,
)


class PermissionSerializer(serializers.ModelSerializer):
    app_name = serializers.SerializerMethodField(
        label='Nombre de app', read_only=True, style={'placeholder': 'Nombre de App'}
    )
    model_name = serializers.SerializerMethodField(
        label='Nombre de modelo',
        read_only=True,
        style={'placeholder': 'Nombre de modelo'},
    )

    @extend_schema_field(OpenApiTypes.STR)
    def get_app_name(self, obj):
        content = ContentType.objects.get(pk=obj.content_type_id)
        return content.app_label.capitalize()

    @extend_schema_field(OpenApiTypes.STR)
    def get_model_name(self, obj):
        content = ContentType.objects.get(pk=obj.content_type_id)
        return content.name.capitalize()

    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer(many=True, read_only=True)
    groups = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        exclude = ('password',)
