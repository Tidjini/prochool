from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api_views import TeacherApiViewSet


router = DefaultRouter()

router.register('teachers', TeacherApiViewSet)

urlpatterns = [
    path('', include(router.urls))
]
