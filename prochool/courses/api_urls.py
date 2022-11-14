from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .api_views import CourseApiViewSet, PresenceApiViewSet

router = DefaultRouter()

router.register('courses', CourseApiViewSet)
router.register('presences', PresenceApiViewSet)

urlpatterns = [
    path('', include(router.urls))
]
