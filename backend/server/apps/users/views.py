from django.contrib.auth.models import Permission
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from users.models import (
    CustomUser,
    Role,
)

from .serializers import (
    CustomUserSerializer,
    PermissionSerializer,
    RoleSerializer,
)


class CustomUserViewSet(viewsets.GenericViewSet, RetrieveModelMixin):
    queryset = CustomUser.objects.all().order_by('id')
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer

    @action(
        detail=False,
        methods=['get'],
        name='Información de usuario',
        url_path='me',
        url_name='personal_information',
    )
    def user_information(self, request):
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        summary='List all permissions',
        description='Return a list of all permissions in the system.',
        tags=['Permissions'],
    ),
    retrieve=extend_schema(
        summary='Retrieve permission',
        description='Get details of a specific permission',
        tags=['Permissions'],
    ),
)
class PermissionViewSet(viewsets.GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Permission.objects.all().order_by('id')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PermissionSerializer


@extend_schema_view(
    list=extend_schema(
        summary='List all roles',
        description='Return a list of all roles in the system.',
        tags=['Roles'],
    ),
    retrieve=extend_schema(
        summary='Retrieve role',
        description='Get details of a specific role',
        tags=['Roles'],
    ),
    create=extend_schema(
        summary='Create a role', description='Create a role', tags=['Roles']
    ),
    update=extend_schema(
        summary='Update a role',
        description='Update details of a specific role',
        tags=['Roles'],
    ),
    partial_update=extend_schema(
        summary='Partial update a role',
        description='Update details of a specific role',
        tags=['Roles'],
    ),
    destroy=extend_schema(
        summary='Delete a role',
        description='Delete a specific role',
        tags=['Roles'],
    ),
)
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('id')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = RoleSerializer
