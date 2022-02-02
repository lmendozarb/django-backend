from django.contrib.auth.forms import UserChangeForm

from .models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        labels = {
            'groups': 'Roles',
        }
