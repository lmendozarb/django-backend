from django.contrib import admin
from django.contrib.auth.admin import (
    GroupAdmin,
    UserAdmin,
)
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm
from .models import (
    CustomUser,
    Role,
)

admin.site.unregister(Group)
admin.site.register(Role, GroupAdmin)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    search_fields = (
        'username',
        'email',
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            _('Personal info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'maternal_last_name',
                    'sex',
                    'email',
                    'document_number',
                    'cellphone',
                    'phone',
                    'address',
                    'work_phone',
                    'work_address',
                    'image',
                )
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    ordering = ('username',)
    list_per_page = 50
