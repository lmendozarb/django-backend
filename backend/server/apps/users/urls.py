from django.urls import (
    include,
    path,
)
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    CustomUserViewSet,
    PermissionViewSet,
    RoleViewSet,
)

app_name = 'users'

router = SimpleRouter()
router.register('users', CustomUserViewSet)
router.register('permissions', PermissionViewSet)
router.register('roles', RoleViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
