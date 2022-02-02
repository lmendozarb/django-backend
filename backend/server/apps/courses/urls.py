from rest_framework.routers import SimpleRouter

from courses.views import (
    CourseByCategory,
    SingleCourseViewSet,
)

app_name = 'courses'
router = SimpleRouter()
router.register(r"category/(?P<slug>[^/.]+)", CourseByCategory)
router.register(r"course/(?P<id>[^/.]+)", SingleCourseViewSet)

urlpatterns = router.urls
